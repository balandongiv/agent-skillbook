"""Mechanical gates for model-drafted manuscript prose.

Every gate answers one question with a yes or no, so a failing draft is rejected and
redrafted rather than hand-patched. Hand-patching is how a wrong number reaches a
submitted paper: the edit looks small, nobody re-audits, and the provenance chain breaks.

Gates provided:

``verify_numbers``
    Every numeric literal in the prose appears in the evidence packet.
``verify_citations``
    Every citation key resolves in the bibliography.
``verify_preserved``
    A structural revision changed no number, citation key, or reference target.
``check_latex_hazards``
    No unescaped ``%`` or ``_`` in text mode - both fail silently or cryptically.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

NUMBER = re.compile(r"\d+(?:\.\d+)?")
CITE = re.compile(r"\\cite[pt]?\*?(?:\[[^\]]*\])*\{([^}]*)\}")
REF = re.compile(r"\\(?:eq)?ref\{([^}]*)\}")
SCI = re.compile(r"(\d+(?:\.\d+)?)[eE]-0*(\d+)")

#: Numbers that are structural rather than measured: section and table numbers, common
#: round parameters, and small integers that appear as ordinary English ("all four").
STRUCTURAL_NUMBERS = {
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
    "20", "30", "40", "50", "60", "95", "100", "120", "1020",
}


@dataclass
class GateResult:
    """Outcome of one gate. ``ok`` is the only thing callers must branch on."""

    ok: bool
    detail: str = ""
    offending: list[str] = field(default_factory=list)

    def __bool__(self) -> bool:
        return self.ok


def _strip_commands(text: str) -> str:
    """Remove citation keys and refs so their digits are not read as measured values."""
    text = CITE.sub(" ", text)
    text = REF.sub(" ", text)
    return re.sub(r"\\[a-zA-Z@]+", " ", text)


def numbers_in(text: str) -> list[str]:
    """Numeric literals a reader would see as measured values."""
    return NUMBER.findall(_strip_commands(text))


def citations_in(text: str) -> set[str]:
    keys: set[str] = set()
    for m in CITE.finditer(text):
        keys.update(k.strip() for k in m.group(1).split(",") if k.strip())
    return keys


def refs_in(text: str) -> set[str]:
    return {m.group(1).strip() for m in REF.finditer(text)}


def packet_numbers(packet: str, extra_allowed: set[str] | None = None) -> set[str]:
    """Every numeric form the prose may legitimately show for this packet.

    A packet value admits its own spellings: ``0.868`` also licenses ``.868``, and
    ``6.51e-09`` licenses the exponent ``9`` because the prose renders it as
    ``6.51\\times10^{-9}``.
    """
    found = set(NUMBER.findall(packet))
    for _mantissa, exponent in SCI.findall(packet):
        found.add(exponent)
    for n in list(found):
        if n.startswith("0."):
            found.add(n[1:])
        if "." in n:
            found.add(n.rstrip("0").rstrip("."))
    return found | (extra_allowed or set())


def verify_numbers(prose: str, packet: str,
                   extra_allowed: set[str] | None = None) -> GateResult:
    """Reject prose containing a number the packet does not support."""
    allowed = packet_numbers(packet, extra_allowed) | STRUCTURAL_NUMBERS
    unknown = []
    for token in numbers_in(prose):
        if token in allowed:
            continue
        if "." in token and token.rstrip("0").rstrip(".") in allowed:
            continue
        unknown.append(token)
    if unknown:
        return GateResult(False, "numbers not in packet", sorted(set(unknown)))
    return GateResult(True)


def bibliography_keys(*bib_paths: Path) -> set[str]:
    keys: set[str] = set()
    for path in bib_paths:
        if path.exists():
            text = path.read_text(encoding="utf-8", errors="replace")
            keys |= {k.strip() for k in re.findall(r"@\w+\{([^,]+),", text)}
    return keys


def verify_citations(prose: str, valid_keys: set[str]) -> GateResult:
    """Reject prose citing a key that does not resolve in the bibliography."""
    unknown = sorted(citations_in(prose) - valid_keys)
    if unknown:
        return GateResult(False, "unresolvable citation keys", unknown)
    return GateResult(True)


def verify_preserved(before: str, after: str, *,
                     allow_new_citations: bool = False) -> GateResult:
    """Reject a structural revision that changed the content.

    Set ``allow_new_citations`` for a citation-attachment pass, where new keys are the
    point but existing ones must survive.
    """
    if sorted(numbers_in(before)) != sorted(numbers_in(after)):
        lost = set(numbers_in(before)) - set(numbers_in(after))
        added = set(numbers_in(after)) - set(numbers_in(before))
        return GateResult(False, "numbers changed",
                          [f"lost:{sorted(lost)}", f"added:{sorted(added)}"])
    if refs_in(before) != refs_in(after):
        return GateResult(False, "reference targets changed",
                          sorted(refs_in(before) ^ refs_in(after)))
    before_cites, after_cites = citations_in(before), citations_in(after)
    if allow_new_citations:
        if not before_cites <= after_cites:
            return GateResult(False, "dropped existing citations",
                              sorted(before_cites - after_cites))
    elif before_cites != after_cites:
        return GateResult(False, "citations changed",
                          sorted(before_cites ^ after_cites))
    return GateResult(True)


def prose_only(text: str) -> str:
    """Reduce LaTeX to the running text a reader sees.

    Math mode, whole-line comments, and command arguments are removed: an underscore is
    legal inside ``\\ref{tab:exp1_main}`` and a ``%`` is legal in a comment, so flagging
    them there is noise that trains people to ignore the gate.
    """
    text = re.sub(r"(?m)^\s*%.*$", " ", text)
    text = re.sub(r"\\\[.*?\\\]", " ", text, flags=re.S)
    text = re.sub(r"(?<!\\)\$[^$]*\$", " ", text)
    return re.sub(r"\\[a-zA-Z@]+\*?(?:\[[^\]]*\])?(?:\{[^{}]*\})*", " ", text)


def check_latex_hazards(text: str) -> GateResult:
    """Reject text-mode ``%`` and ``_``.

    An unescaped ``%`` does not raise a LaTeX error - it comments out the rest of the
    line and silently removes content from the PDF, which is the worst possible failure
    mode. An unescaped ``_`` fails loudly with "Missing $ inserted".
    """
    body = prose_only(text)
    problems = []
    for symbol in ("_", "%"):
        for m in re.finditer(rf"(?<!\\){re.escape(symbol)}", body):
            context = " ".join(body[max(0, m.start() - 40):m.start() + 20].split())
            problems.append(f"{symbol!r}: ...{context}...")
    if problems:
        return GateResult(False, "unescaped LaTeX special characters", problems)
    return GateResult(True)


def first_sentence(text: str) -> str:
    """The paragraph's topic sentence, for transition chaining and revision checks."""
    clean = re.sub(r"\s+", " ", text.strip())
    m = re.search(r"^(.{40,}?[.!?])(?:\s|$)", clean)
    return (m.group(1) if m else clean)[:300]


def _fix_scientific_notation(text: str) -> str:
    """Rewrite ``4.97e-10`` as LaTeX, adding math delimiters only where they are missing.

    Splitting on existing ``$...$`` spans is what keeps this correct: inside math the
    replacement must stay bare, outside it must bring its own delimiters, and emitting the
    wrong one either fails to compile or produces nested ``$``.
    """
    parts = re.split(r"(\$[^$]*\$)", text)
    for i, part in enumerate(parts):
        if part.startswith("$") and part.endswith("$"):
            parts[i] = SCI.sub(lambda m: rf"{m.group(1)}\times10^{{-{m.group(2)}}}", part)
        else:
            parts[i] = SCI.sub(lambda m: rf"${m.group(1)}\times10^{{-{m.group(2)}}}$", part)
    return "".join(parts)


def repair_rendered_latex(text: str) -> str:
    """Undo what the ChatGPT UI does to LaTeX on its way through the renderer.

    The UI returns rendered text: inline math arrives bare, scientific notation keeps its
    Python spelling, minus signs become U+2212, and line breaks land mid-sentence.
    """
    text = re.sub(r"\(\s*\n\s*", "(", text)
    text = re.sub(r"\s*\n\s*(?=(?:p|r|F1|CCC|=|\[|\+?\d))", " ", text)
    text = text.replace("\u2212", "-").replace("\u2013", "--")
    text = _fix_scientific_notation(text)
    text = re.sub(r"\bLin(?:'s)? CCC\s*=\s*([0-9.]+)", r"Lin's CCC $=\1$", text)
    text = re.sub(r"\bPearson\s+r\s*=\s*([0-9.]+)", r"Pearson $r=\1$", text)
    text = re.sub(r"(?<![A-Za-z$])p\s*=\s*([0-9.]+)", r"$p=\1$", text)
    text = re.sub(r"(?<![$_{\\A-Za-z])\bF1\b", "$F_1$", text)
    text = re.sub(r"(?<!\\)%", r"\\%", text)
    return text.replace("$$", "$").strip() + "\n"
