# Test Prompts: Academic LaTeX Paragraph Writer (ChatGPT UI)

These prompts should trigger this skill when entered into an AI agent that has it loaded.

---

## Test Prompt 1

> Write the results section for this paper using the ChatGPT UI, one paragraph per LaTeX file.

Expected behavior: Run the ChatGPT UI smoke gate first; build an evidence packet per paragraph
from the verified artifacts; draft one paragraph per fresh chat; gate each draft's numbers and
citation keys; install each into its own `paragraph.tex` wired through `\input{}`.

---

## Test Prompt 2

> Make sure every paragraph starts with a topic sentence and flows from the one before it.

Expected behavior: Run a structural revision pass in manuscript reading order, feeding each
paragraph its predecessor's opening sentence, under a preservation gate that rejects any change
to numbers, citation keys, or reference targets.

---

## Test Prompt 3

> Draft the discussion paragraphs — only cite papers that are already in the bibliography.

Expected behavior: Extract the closed list of resolvable citation keys with titles and years,
supply it in the prompt, and reject any draft citing a key outside that list.

---

## Test Prompt 4

> The median estimator didn't actually beat the mean. Rewrite that paragraph.

Expected behavior: State the negative result explicitly in the task text so the model reports it
plainly rather than softening it, and verify the resulting prose does not claim support for the
failed hypothesis.

---

## Test Prompt 5

> The paragraph came back from ChatGPT with `p=1` and `95%` in it — install it.

Expected behavior: Repair the rendered-text artifacts before installing (`$p=1$`, `95\%`,
scientific notation, Unicode minus, mid-sentence line breaks), then run the LaTeX hazard gate,
recognising that an unescaped `%` silently deletes content rather than raising an error.

---

## Test Prompt 6

> Add these newly found references to the discussion.

Expected behavior: Attach citations only where a paragraph already makes a claim they support,
under a gate that preserves numbers and existing citations and leaves the topic sentence intact;
drop candidates that support no existing claim rather than padding the section.
