---
name: implementation-aligned-planning
description: Turn ambiguous, half-baked, or outdated plans into living planning docs aligned with code, config, paths, naming contracts, execution flow, caches, EDA outputs, and debugging navigation.
---

# Implementation-Aligned Planning

Use this skill when a repository has planning documents that are ambiguous, stale, or only half-baked, and the user wants them turned into trustworthy working documents. The goal is to make planning docs useful for implementation, review, and navigation, not to preserve vague aspirations that no longer match the code. Good implementation-aligned docs should also explain naming conventions, source-versus-cache relationships, and which debug/tutorial entrypoints humans should use.

---

## Core principles

### 1. Treat plans as living documents

A plan is not immutable. If implementation, configuration, naming, folder structure, or execution order changed, the planning docs should change too.

### 2. Separate intent from verified behavior

Use the existing plan to recover intent. Use code, config, and generated artifacts to recover actual behavior. When they disagree, resolve the disagreement explicitly instead of blending them together.

### 3. Turn ambiguity into explicit contracts

A useful stage plan should say exactly:

- what the stage guarantees
- what it does not do
- what it reads
- what it writes
- which modules and functions implement it
- the authoritative execution order

### 4. Prefer code and config as the source of truth for concrete details

When concrete details such as paths, file names, cache rules, CLI flags, or artifact names are already implemented, document the implementation truthfully. Do not keep outdated planning text just because it was written first.

### 5. Write for repository navigation, not only for aspiration

A strong planning document should help a reader answer:

- where do I start reading the code
- what function runs first
- what files are inputs and outputs
- what checks happen
- where are common failures raised
- how do I debug this stage

### 6. Document naming contracts explicitly

If a stage emits wide tables, threshold sweeps, modality-prefixed features, or multiple experiment labels, document the naming rules. A good planning doc should answer:

- how columns are prefixed by modality or stage
- how threshold or parameter variants are encoded in names
- how experiment-specific label columns are named
- how report or EDA artifact names differ from heavy plot galleries

### 7. Document source-of-truth files separately from runtime caches

When a slow or manual source is normalized into a faster runtime cache, document both:

- the human or raw source of truth
- the derived cache or normalized format actually used during execution

This prevents confusion such as "the code reads parquet but the project source is an Excel workbook."

### 8. Synchronize related docs, not only the stage file

When one stage document changes materially, also inspect the related shared docs such as:

- `folder_structure.md`
- `Project_Execution_Flowchart.md`
- hash or execution docs
- README or runbook docs when affected

### 9. Keep unresolved points visible

If something is genuinely not discoverable from the repo, do not invent certainty. Mark the unresolved point clearly and keep the rest of the document explicit.

---

## Step-by-step process

### Step 1: Read the existing planning docs first

Before rewriting anything, read:

- the stage planning document itself
- shared flowchart and folder-structure docs
- any hash, runbook, or execution documents that relate to the stage

This reveals both the intended story and the current inconsistencies.

### Step 2: Inspect the real implementation

Read the code and config that actually drive the stage:

- entrypoint modules
- helper modules
- path-resolution utilities
- config files
- summary or manifest outputs when useful

Build the doc from verified behavior, not from memory.

### Step 3: Make a discrepancy list

Record the mismatches between plan and implementation, for example:

- wrong file names
- outdated folder layout
- missing cache rules
- renamed stages
- changed CLI flags
- new outputs
- removed steps

Resolve each mismatch deliberately.

### Step 4: Choose the source of truth for each mismatch

Use these defaults:

- **code/config/artifacts** for concrete behavior
- **planning docs** for the original intent
- **explicit notes** for unresolved items

If the user has not asked for a behavior change, update the doc to match the implementation rather than pretending the old plan is still current.

### Step 5: Rewrite the stage doc into a stable structure

When a stage document needs to become implementation-aligned, prefer this structure:

1. `# 0) What this stage guarantees (contract)`
2. `## 1) Folder contract`
3. `## 2) Naming contract`
4. `## 3) Python modules & functions responsible (implementation map)`
5. `## 4) Execution flow (authoritative) - with function calls`
6. `## 5) Required existence checks`
7. `## 6) Common failure modes`
8. `## 7) Minimal pseudocode`
9. `## 8) Debugging path for repository navigation`

This format turns a vague plan into a document that is both executable in the reader's head and useful during debugging.

### Step 6: Rewrite shared docs when the change affects them

After updating the stage document, sync the related shared docs when needed:

- update `folder_structure.md` if folder comments or file locations changed
- update `Project_Execution_Flowchart.md` if behavior, stages, or artifacts changed
- update hash or runbook docs if naming or output scope changed

### Step 7: Make the doc easy to diff against code

Prefer:

- real module paths
- real function names
- real artifact names
- real column and artifact naming prefixes
- explicit source-versus-cache relationships
- explicit read/write lists
- exact stage boundaries

Avoid vague wording like "some feature extraction happens here."

### Step 8: Preserve useful open questions without leaving the whole doc fuzzy

If the repo still leaves some things unresolved, isolate them in a short open-question or assumption note. Do not let one unknown make the whole plan vague.

---

## Rules

- Always read the current plan before rewriting it.
- Always inspect the implementation before claiming the plan is correct.
- Always prefer code and config for concrete path, artifact, and execution details.
- Always rewrite ambiguous prose into explicit stage contracts.
- Always document naming conventions when columns, reports, or experiment outputs are pattern-based.
- Always document both the source-of-truth file and the runtime cache when they differ.
- Always update related shared docs when behavior or artifacts changed.
- Always call out unresolved points explicitly instead of inventing certainty.
- Never leave a planning doc half updated after implementation changed.
- Never preserve wrong details just because they are already written down.

---

## Common mistakes to avoid

- **Documenting the intended future instead of the current reality**: A plan that does not match the repo is harmful.
- **Updating only one file**: Stage docs, folder docs, and flowcharts often drift together.
- **Using vague verbs**: "process," "handle," and "prepare" hide important steps. Name the actual operations.
- **Omitting read/write contracts**: Readers need to know which files enter and leave the stage.
- **Leaving naming conventions implicit**: Wide feature tables and experiment outputs become much harder to navigate.
- **Documenting only the fast cache**: Readers still need to know the original workbook, CSV, or manual source of truth.
- **Ignoring failure paths**: A good plan should explain what blocks success and where to debug first.
- **Leaving function names out**: Without real modules and functions, the doc is not a navigation tool.
- **Pretending ambiguity is precision**: If something is truly unknown, mark it rather than guessing.

---

## Condensed checklist

- Read the old plan and the shared docs.
- Inspect the real code, config, and artifacts.
- Make a discrepancy list.
- Use code and config as the source of truth for concrete behavior.
- Rewrite the stage into contract, folder, naming contract, implementation map, execution flow, checks, failure modes, pseudocode, and debug path.
- Sync shared docs such as flowchart and folder structure when needed.
- Mark unresolved items explicitly.
- Leave the planning docs more navigable than you found them.
