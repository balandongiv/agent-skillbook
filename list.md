# Skill Catalog

All reusable skills in this repository and what each is for. Edit the canonical files under
`skills/<slug>/` and run `python -m agent_skillbook.cli render` to regenerate the platform exports.

_26 skills (purpose text taken from each skill's `skill.yaml` summary)._

| Skill | Purpose |
|---|---|
| `atomise-claims` | Decompose any sentence, paragraph, or section into atomic, independently checkable factual claims so each can be verified, cited, or revised on its own. |
| `beginner-moodle-programming-question` | Generate beginner-friendly Moodle programming questions with tag clarification, partial answer-preload scaffolding, auto-created test cases, actionable hints, and feedback on common beginner mistakes. |
| `citation-audit` | Decompose cited statements into atomic claims, cross-check whether each cited paper actually supports the claim, extract the exact supporting text from the abstract or full paper, and emit a structured JSON citation audit. |
| `code-readability-best-practices` | Review and refactor code for top-down readability by reorganizing functions, grouping related helpers, and rewriting noisy comments without changing behavior. |
| `experiment-runbook-discipline` | Plan, launch, monitor, and document long-running experiments or validation sweeps with smallest-real-data smoke scopes, fresh experiment prefixes, live status artifacts, rolling logs, and promotion to full runs only after explicit pass criteria are met. |
| `find-extra-analysis` | Given a paper's abstract or results section, propose additional analyses that would strengthen, stress-test, or extend the work, ranked by value and feasibility, in a domain-general way. |
| `good-description-writing` | Write precise, specific descriptions for agent skills, tools, and functions so that AI agents can route to them accurately. |
| `good-function-design` | Write small, readable, testable Python functions with clear names and explicit inputs and outputs. |
| `handoff` | Create operational handoff markdowns that capture what was completed, what is stopped, what remains pending, which artifacts matter, and which commands the next agent should run next. |
| `handoff-resume` | Resume repository work from an existing handoff markdown by reading it first, executing pending tasks in order, and marking completed tasks `Done? = Yes` only when concrete evidence exists. |
| `hyperparameter-search-strategy` | Choose efficient hyperparameter search strategies (random search, Bayesian optimization, successive halving, evolutionary, population-based) over brute-force grids when tuning under compute and evaluation-cost constraints. |
| `implementation-aligned-planning` | Turn ambiguous, half-baked, or outdated plans into living planning docs aligned with code, config, paths, naming contracts, execution flow, caches, EDA outputs, and debugging navigation. |
| `intellij-line-debugging` | Turn complex execution paths into line-by-line IntelliJ IDEA debugging flows with serial tutorial entrypoints, smallest-real-input reruns, exact breakpoint order, and deliberate stepping into editable local dependencies. |
| `literature-review-writing` | Write or expand a literature review / related-work section using only a provided knowledge library (CSV or SQLite), citing only keys that exist there, with no invented papers, facts, or citation keys. |
| `manuscript-final-qc` | Run a final pre-submission gate on a LaTeX manuscript — clean compile, zero undefined citations/references, no forbidden domain terms, no leaked draft/editorial notes in the rendered PDF, and numeric spot-checks against source artifacts. |
| `manuscript-results-curation` | Curate manuscript results directly in LaTeX from experiment artifacts — tables, plots, graphs, images, and detailed scientific interpretation tied to concrete outputs. |
| `mne-blink-report-html` | Generate an MNE HTML report that plots blink windows one by one from epoch data, with configurable padding, channel sets, and subset selection such as true positives, false negatives, or false positives. |
| `python-class-and-filename` | Create focused Python classes and choose matching snake_case module filenames when adding or refactoring class-based code. |
| `real-data-validation-promotion` | Validate data or ML pipelines on the smallest real dataset scope first, then promote to staged batches and full sweeps with the same code path, editable local dependencies, artifact checks, and honest residual-risk reporting. |
| `repo-readme-writing` | Write clear, structured, beginner-friendly README files for GitHub repositories that explain purpose, setup, and usage. |
| `strategy-c-experiment-log` | Ensure every exploratory experiment tied to Strategy C gets a structured entry in the Strategy C observation log so future agents see consistent history. |
| `strategy-impact-log` | Record and track strategy proposals, code changes, performance metrics, issues, and their cumulative effects on final results — a durable audit trail of what was tried, what worked, and what didn't. |
| `subject-outlier-review` | Review per-subject performance to identify likely outliers, distinguish bad data from difficult-but-valid cases, and document whether subject exclusion is justified before any filtered rerun. |
| `telegram-heartbeat` | Add a secret-safe Telegram heartbeat and notification layer to a long-running agent, with periodic health heartbeats, immediate urgent alerts, milestone updates, and anti-spam rate limiting. |
| `write-discussion-section` | Draft or revise a discussion section that interprets the reported results without overclaiming, using hedged causal and novelty language, an honest limitations paragraph, and no numbers beyond those already in the results. |
| `write-results-section` | Draft or revise a results section as factual, number-grounded prose where every figure comes from verified artifacts (CSV/stats files), every table and figure is referenced and explained, and no number is invented. |
