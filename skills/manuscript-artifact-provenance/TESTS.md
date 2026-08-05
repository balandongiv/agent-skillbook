# Test Prompts: Manuscript Artifact Provenance and Generator Naming

These prompts should trigger this skill when entered into an AI agent that has it loaded.

---

## Test Prompt 1

> Clean up the analysis scripts — I can't tell which one generates which table.

Expected behavior: Inventory the artifacts the manuscript actually uses, write the
artifact → generator map, rename each generator for the artifact it produces, and split
monolithic scripts.

---

## Test Prompt 2

> We only kept three of the eight experiments. Remove the rest.

Expected behavior: Delete the dropped experiments' scripts, configs, generated `.tex`, `\input`
lines, and LaTeX sections together, then confirm the manuscript still compiles with no undefined
references.

---

## Test Prompt 3

> There are four run directories. Which one backs the paper?

Expected behavior: Establish one source-of-truth results directory, verify what it actually
contains, encode it in config, and repoint every generator at it.

---

## Test Prompt 4

> Regenerate all the tables and figures.

Expected behavior: Run every generator through the manifest, verify each output file was written
and is non-empty, and check the artifacts rather than trusting exit codes.

---

## Test Prompt 5

> This table looks empty in the PDF.

Expected behavior: Check the generator's filter values against the actual CSV column values, and
make the data layer raise on an empty selection rather than emitting an empty table.

---

## Test Prompt 6

> Set up the results pipeline so it stays reproducible as we revise.

Expected behavior: Single source-of-truth directory, shared data layer, artifact-named
generators, provenance comments in generated files, and a manifest with a `check` command run
before every submission build.
