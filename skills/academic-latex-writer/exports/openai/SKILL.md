---
name: academic-latex-writer
description: Draft manuscript prose by driving the ChatGPT web UI one paragraph at a time, writing LaTeX only, storing each paragraph in its own file, and enforcing a topic-sentence-first structure — with mechanical gates that reject any draft containing a number, citation key, or reference the supplied evidence packet does not support.
---

# Academic LaTeX Paragraph Writer (ChatGPT UI)

## Overview

Manuscript prose is drafted by routing the *writing* to the ChatGPT web UI while the orchestrating
agent keeps control of every fact. The model never computes, rounds, or recalls a number: it receives
an **evidence packet** of pre-computed values and may use nothing else. Each paragraph is produced in
its own chat, lands in its own `.tex` file, opens with a topic sentence, and passes a mechanical gate
before it is installed. The result is prose that reads as one voice and whose every value traces back
to a verified artifact.

This skill is the *authoring loop*. It composes with `write-results-section` and
`write-discussion-section` (which say **what** each section should contain),
`latex-structure-enforcer` (which migrates legacy flat files into the per-paragraph layout), and
`manuscript-final-qc` (the final compile gate).

## Core principles

1. **The topic sentence carries the paragraph.** Every paragraph begins with a sentence stating its
   main idea. Every remaining sentence explains, supports, or develops that idea. A paragraph must
   never open with an isolated detail, a citation, an example, a bare cross-reference
   ("X is shown in Figure 3"), or background laid down before the point is made. Where a paragraph
   follows another, the topic sentence carries a transition that connects them.
2. **One paragraph, one file.** Each paragraph lives at `<section>/<name>/paragraph.tex` and is wired
   in through `\input{}`. Small files make a paragraph reviewable, revisable, and revertible on its
   own, and they make "which paragraph broke the build" a one-line answer.
3. **The model writes; it does not calculate.** Every number the prose may contain is supplied
   verbatim in an evidence packet built by code from the source artifacts. The model is forbidden to
   round, re-scale, derive, or infer a value. If the packet does not support a claim, the claim is not
   made.
4. **Gate before installing, never patch after.** A draft that contains an unverified number, an
   unresolvable citation key, or a broken reference is rejected and redrafted — not silently repaired.
   Rejection is cheap; a wrong number in a submitted paper is not.
5. **Restructuring must not change meaning.** A revision pass for structure runs against a
   preservation gate: the set of numbers, citation keys, and `\ref` targets must be identical before
   and after. This makes it safe to improve paragraph shape late, without re-auditing the content.
6. **Honesty outranks the narrative.** When the evidence contradicts a stated hypothesis, the
   paragraph says so plainly. Instruct the model explicitly when a result is negative, or it will
   soften the finding into a partial success on its own.

## Step-by-step process

1. **Run the smoke gate first.** `python resources/smoke_chatgpt_ui.py` from the
   `chatgpt-ui-reasoning` skill. If it fails (login lost, driver/Chrome mismatch, stale lockfile), fix
   the session before any drafting.
2. **Build the evidence packets.** Write a script that computes, from the verified artifacts, one text
   packet per planned paragraph containing every value that paragraph may cite. Nothing in a packet is
   model-generated. Keep the packets on disk — they are the audit record and the input to the gate.
3. **Build the citable-key list.** Extract every citation key that resolves in the bibliography, with
   title and year. The model may cite only from this closed list.
4. **Plan the paragraph map** before drafting: one entry per paragraph, in manuscript reading order,
   each naming its `.tex` directory, its packet(s), and the single idea it must carry. Create the
   directories with placeholder files so the document still compiles mid-flight.
5. **Draft one paragraph per chat.** Send the style contract + the topic-sentence rule + the task +
   the packet + the citable keys. Open a fresh chat per paragraph so contexts never bleed. Save the
   raw transcript before parsing.
6. **Gate each draft**: every numeric literal must appear in its packet; every citation key must
   resolve; the output must be LaTeX body text only.
7. **Install** passing drafts into their `paragraph.tex` files, normalising anything the UI mangles
   (see *LaTeX hazards* below).
8. **Revise for structure in reading order.** Feed each paragraph its predecessor's opening sentence
   so the transition connects to what actually precedes it. Tell section-opening paragraphs that they
   open a subsection, so they do not invent a false transition. Run the preservation gate on every
   revision.
9. **Compile and verify**: build the document, confirm zero undefined references and citations, and
   re-run the number audit after any edit.

## Rules

- Always begin every paragraph with a topic sentence that states the paragraph's main idea, and make
  every following sentence serve it.
- Always carry a transition in the topic sentence when a paragraph follows another; never manufacture
  one for a paragraph that opens a section.
- Never let a paragraph open with an isolated detail, a citation, an example, a bare cross-reference,
  or background before the main point.
- Always write one paragraph per `.tex` file; never concatenate paragraphs into a single file.
- Always supply every permitted number in an evidence packet; never let the model compute or recall one.
- Always restrict citations to a closed list of keys that already resolve in the bibliography.
- Always reject and redraft a failing draft; never hand-patch a number into a draft that failed the gate.
- Always run a preservation gate on structural revisions (numbers, citation keys, `\ref` targets
  unchanged).
- Always state a negative or hypothesis-contradicting result plainly, and say so explicitly in the prompt.
- Always open a fresh chat per paragraph and save the raw transcript before parsing.
- Never let the model add sentences that summarise cited papers; a citation supports an existing claim.

## LaTeX hazards this loop must neutralise

The ChatGPT UI returns *rendered* text, not LaTeX source. Post-process every reply:

- **Unescaped `%`** — LaTeX does **not** error; it comments out the rest of the line and silently
  deletes content from the PDF. Escape it, and check for it as a standing gate.
- **Bare inline math** — `p=1`, `F1`, `r=0.918`, `95%` come back as plain text. Restore `$p=1$`,
  `$F_1$`, `$r=0.918$`, `95\%`.
- **Python scientific notation** — packet values like `4.97e-10` are reproduced literally. Render as
  `$4.97\times10^{-10}$`.
- **`p = 0.000`** — reads as exactly zero. Render as `$<0.001$`, in both the prose and the generating
  table code.
- **Unicode minus (U+2212) and en-dashes** used as minus signs will not compile.
- **Renderer line breaks** land mid-sentence, often immediately before inline math. Rejoin them.
- **Dropped colons** — replies have come back with `\ref{tab}` for `\ref{tab:error-structure}`. Verify
  every `\ref` target against a real label after each batch.
- **Raw identifiers with underscores** (session IDs, filenames) must be escaped or wrapped in
  `\texttt{}`, or the build fails with "Missing $ inserted".
- **Never write LaTeX through a shell heredoc.** `\a` in `\addbibresource` becomes a literal BEL byte
  (0x07), silently disabling the line with no error. Use file-writing tools or a real script file.

## Common mistakes to avoid

- **Letting the model do arithmetic** — it will produce a plausible, wrong number. Compute in code.
- **Opening with a pointer** — "Table 4 shows the comparison" is not a topic sentence; it states where
  something is, not what is true.
- **Revising structure and content in one pass** — you lose the ability to gate either. Draft, then
  restructure separately under a preservation gate.
- **Bulk-importing a literature search** — a keyword sweep returns hundreds of hits; citations that
  support no claim weaken a section. Screen on title, then cite only what a paragraph argues.
- **Trusting a clean exit code** — the worst LaTeX failures (unescaped `%`, BEL byte, dropped colon)
  produce a successful build with missing content. Check artifacts, not return codes.
- **Reusing one chat for many paragraphs** — contexts bleed and the model starts cross-referencing
  paragraphs it should not know about.
- **Padding to a word count** — a short paragraph that develops one idea beats a long one that drifts.

## Additional guidance

Expect roughly three minutes per paragraph and about 25 sends before the UI session needs restarting;
plan batches accordingly and make the runner resumable by skipping paragraphs whose draft already
exists. Keep every packet, prompt, and raw reply — when a reviewer asks where a number came from, the
chain is: artifact → packet → prompt → reply → installed paragraph.

`resources/` ships a working implementation of this loop (`paragraph_writer.py`) plus the gates
(`prose_gates.py`). Import them rather than rewriting the pipeline each session.
