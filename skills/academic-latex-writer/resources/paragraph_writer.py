"""Draft and revise manuscript paragraphs through the ChatGPT UI, one file each.

Import this instead of rewriting the loop. It supplies the style contract (including the
topic-sentence rule), drives one fresh chat per paragraph, applies the gates from
``prose_gates``, and installs only what passes.

    from paragraph_writer import Paragraph, draft_all, revise_for_structure

    plan = [
        Paragraph("r1_main", packets=["r1_main"],
                  task="Report the headline comparison ...",
                  position="opens the Results section"),
        Paragraph("r2_stability", packets=["r2_stability"],
                  task="Report stability across epoch durations ..."),
    ]
    draft_all(plan, packet_dir=Path("packets"), out_dir=Path("writing/e_result"))
    revise_for_structure(plan, out_dir=Path("writing/e_result"))

Run the ``chatgpt-ui-reasoning`` smoke gate before either call.
"""
from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

from prose_gates import (  # noqa: E402  - resources dir is on sys.path by convention
    GateResult,
    bibliography_keys,
    first_sentence,
    repair_rendered_latex,
    verify_citations,
    verify_numbers,
    verify_preserved,
)

# The session class ships with the chatgpt-ui-reasoning skill; point at it once.
CHATGPT_RESOURCES = Path(
    r"C:\Users\balan\IdeaProjects\agent-skillbook\skills\chatgpt-ui-reasoning\resources"
)
if str(CHATGPT_RESOURCES) not in sys.path:
    sys.path.insert(0, str(CHATGPT_RESOURCES))

MIN_DRAFT_CHARS = 200

#: The paragraph-structure contract. This is the part of the prompt that must never be
#: softened: it is what makes a section read as an argument rather than a list of facts.
TOPIC_SENTENCE_RULE = r"""PARAGRAPH STRUCTURE (mandatory):
- Begin the paragraph with a clear topic sentence that states its main idea.
- Every remaining sentence must directly explain, support, or develop that topic sentence.
- Do NOT begin with an isolated detail, a citation, an example, a bare cross-reference
  ("X is shown in Figure 3"), or background information laid down before the main point is
  established. A cross-reference may appear in the topic sentence only as a parenthetical
  attached to a claim, never as the claim itself.
- Where this paragraph follows another, carry a transition in the topic sentence that
  connects the two logically."""

STYLE_CONTRACT = r"""You are drafting ONE paragraph of a submitted academic journal article.

REGISTER:
- Plain declarative academic prose. Past tense for what was done and measured.
- NOT Nature/Science house style: no "Here we show", no "strikingly", "remarkably",
  "crucially", "sheds light on"; no rhetorical questions; no opening hook; no closing
  flourish about impact.
- LaTeX body text only. Use \ref{...} for cross-references and ~ before \ref and \cite.

{topic_rule}

HARD RULES ON EVIDENCE:
- Use ONLY numbers that appear literally in the DATA PACKET below. Do not round, re-scale,
  recompute, or derive any number. A difference or ratio must already be in the packet.
- Cite ONLY keys from the CITEABLE KEYS list. Never invent a citation key. If no listed key
  supports a claim, make the claim without a citation or omit it.
- Do not claim anything the packet does not support. Where the task says a result is
  negative or contradicts a hypothesis, say so plainly; do not soften it.

OUTPUT CONTRACT:
- Output ONLY the LaTeX paragraph, between the lines BEGIN_TEX and END_TEX.
- No preamble, no explanation, no markdown fences, no headings, no commentary."""

REVISION_CONTRACT = r"""You are revising ONE paragraph of a submitted academic journal
article. This is a STRUCTURAL revision for paragraph coherence, NOT a rewrite of content.

{topic_rule}

WHAT YOU MUST NOT CHANGE:
- Every numeric value must survive unchanged. Do not round, recompute, add, or drop one.
- Every \cite key and every \ref target must survive unchanged.
- Do not change any claim, hedge, or the direction of a result. If the paragraph says a
  hypothesis was not supported, the revision must still say that.

REGISTER: unchanged - plain declarative academic prose, past tense, not Nature house style.

OUTPUT CONTRACT:
- Output ONLY the revised LaTeX paragraph, between the lines BEGIN_TEX and END_TEX.
- No preamble, no explanation, no commentary on what you changed."""


@dataclass
class Paragraph:
    """One paragraph: its own directory, its own evidence, its own single idea."""

    name: str
    task: str
    packets: list[str] = field(default_factory=list)
    #: Set when the paragraph opens a section, so it does not invent a false transition.
    position: str | None = None

    def path(self, out_dir: Path) -> Path:
        return out_dir / self.name / "paragraph.tex"


def extract_tex(reply: str) -> str:
    """Pull the paragraph out of the reply, tolerating a missing contract marker."""
    m = re.search(r"BEGIN_TEX\s*(.*?)\s*END_TEX", reply, re.S)
    body = m.group(1) if m else reply
    return re.sub(r"^```(?:latex|tex)?\s*|\s*```$", "", body.strip(), flags=re.M).strip()


def load_packet(packet_dir: Path, names: list[str]) -> str:
    if not names:
        return ("(no numeric packet - this paragraph must not contain any measured value)")
    return "\n\n".join(
        (packet_dir / f"{n}.txt").read_text(encoding="utf-8") for n in names
    )


def _install(paragraph: Paragraph, out_dir: Path, body: str) -> None:
    path = paragraph.path(out_dir)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(repair_rendered_latex(body), encoding="utf-8")


def draft_all(plan: list[Paragraph], *, packet_dir: Path, out_dir: Path,
              bib_paths: tuple[Path, ...] = (), citeable: str = "",
              transcripts: Path | None = None, resume: bool = True) -> dict:
    """Draft each planned paragraph in its own chat, gate it, and install what passes.

    ``resume`` skips paragraphs whose file already holds real prose, so a run interrupted
    by the UI's per-session send limit can simply be re-run.
    """
    from chatgpt_ui_session import ChatGPTSession  # noqa: PLC0415  - optional dependency

    transcripts = transcripts or (out_dir.parent / "_transcripts")
    transcripts.mkdir(parents=True, exist_ok=True)
    valid_keys = bibliography_keys(*bib_paths) if bib_paths else set()

    done, failed, skipped = [], [], []
    with ChatGPTSession() as session:
        for paragraph in plan:
            path = paragraph.path(out_dir)
            if resume and path.exists():
                current = path.read_text(encoding="utf-8").strip()
                if len(current) > MIN_DRAFT_CHARS and not current.startswith("%"):
                    skipped.append(paragraph.name)
                    continue

            packet = load_packet(packet_dir, paragraph.packets)
            prompt = "\n\n".join([
                STYLE_CONTRACT.format(topic_rule=TOPIC_SENTENCE_RULE),
                f"===== TASK =====\n{paragraph.task.strip()}",
                f"===== DATA PACKET (the only numbers you may use) =====\n{packet}",
                *([f"===== CITEABLE KEYS (the only keys you may cite) =====\n{citeable}"]
                  if citeable else []),
            ])

            print(f"\n>>> {paragraph.name} ...", flush=True)
            try:
                session.new_chat()
                reply = session.ask(prompt, label=paragraph.name)
            except Exception as exc:  # noqa: BLE001 - a dead chat must not kill the run
                print(f"    FAILED: {type(exc).__name__}: {exc}")
                failed.append(paragraph.name)
                continue

            (transcripts / f"{paragraph.name}.prompt.txt").write_text(prompt, encoding="utf-8")
            (transcripts / f"{paragraph.name}.reply.txt").write_text(reply, encoding="utf-8")

            body = extract_tex(reply)
            gate = _gate_draft(body, packet, valid_keys)
            if not gate:
                print(f"    REJECTED: {gate.detail} {gate.offending}")
                failed.append(paragraph.name)
                continue

            _install(paragraph, out_dir, body)
            print(f"    ok ({len(body.split())} words)")
            done.append(paragraph.name)

    print(f"\ndrafted={len(done)} failed={len(failed)} skipped={len(skipped)}")
    if failed:
        print("FAILED:", failed)
    return {"done": done, "failed": failed, "skipped": skipped}


def _gate_draft(body: str, packet: str, valid_keys: set[str]) -> GateResult:
    if len(body) < MIN_DRAFT_CHARS:
        return GateResult(False, f"suspiciously short ({len(body)} chars)")
    numbers = verify_numbers(body, packet)
    if not numbers:
        return numbers
    if valid_keys:
        return verify_citations(body, valid_keys)
    return GateResult(True)


def revise_for_structure(plan: list[Paragraph], *, out_dir: Path,
                         transcripts: Path | None = None) -> dict:
    """Second pass: enforce topic-sentence structure without altering content.

    Paragraphs are revised in reading order and each is given its predecessor's opening
    sentence, so the transition connects to what actually precedes it in the document
    rather than to whatever the model imagines.
    """
    from chatgpt_ui_session import ChatGPTSession  # noqa: PLC0415

    transcripts = transcripts or (out_dir.parent / "_transcripts_revise")
    transcripts.mkdir(parents=True, exist_ok=True)

    previous_topic: str | None = None
    changed, failed, skipped = [], [], []

    with ChatGPTSession() as session:
        for paragraph in plan:
            path = paragraph.path(out_dir)
            if not path.exists():
                skipped.append(paragraph.name)
                continue
            current = path.read_text(encoding="utf-8").strip()
            if len(current) < MIN_DRAFT_CHARS or current.startswith("%"):
                skipped.append(paragraph.name)
                continue

            context = []
            if paragraph.position:
                context.append(f"POSITION: This paragraph {paragraph.position}.")
            if previous_topic:
                context.append(
                    "PRECEDING PARAGRAPH'S OPENING SENTENCE (transition from this idea; "
                    f"do not repeat it):\n  {previous_topic}"
                )
            else:
                context.append("There is no preceding body paragraph to transition from.")

            prompt = "\n\n".join([
                REVISION_CONTRACT.format(topic_rule=TOPIC_SENTENCE_RULE),
                "===== CONTEXT =====\n" + "\n\n".join(context),
                f"===== PARAGRAPH TO REVISE =====\n{current}",
            ])

            print(f"\n>>> {paragraph.name} ...", flush=True)
            try:
                session.new_chat()
                reply = session.ask(prompt, label=paragraph.name)
            except Exception as exc:  # noqa: BLE001
                print(f"    FAILED: {type(exc).__name__}: {exc}")
                failed.append(paragraph.name)
                previous_topic = first_sentence(current)
                continue

            (transcripts / f"{paragraph.name}.reply.txt").write_text(reply, encoding="utf-8")
            revised = extract_tex(reply)

            gate = verify_preserved(current, revised)
            if len(revised) < MIN_DRAFT_CHARS:
                print(f"    REJECTED: suspiciously short ({len(revised)} chars)")
                failed.append(paragraph.name)
            elif not gate:
                print(f"    REJECTED: {gate.detail} {gate.offending}")
                failed.append(paragraph.name)
            else:
                _install(paragraph, out_dir, revised)
                print(f"    ok — topic: {first_sentence(revised)[:110]}")
                changed.append(paragraph.name)
                current = revised

            previous_topic = first_sentence(current)

    print(f"\nrevised={len(changed)} failed={len(failed)} skipped={len(skipped)}")
    if failed:
        print("FAILED (left unchanged):", failed)
    return {"changed": changed, "failed": failed, "skipped": skipped}


def write_input_wiring(plan: list[Paragraph], *, section_file: Path,
                       input_prefix: str) -> None:
    """Emit the ``\\input{}`` chain so the per-paragraph files actually compile."""
    lines = [f"\\input{{{input_prefix}/{p.name}/paragraph}}" for p in plan]
    section_file.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {len(lines)} \\input lines -> {section_file}")
