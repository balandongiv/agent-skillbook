# Examples — Evidence-Driven Thesis Writer

## Example 1: Building evidence JSON for Section 2.4

### Input (from SQLite screening_decisions)
```json
{
  "paper_id": 317,
  "decision": "include",
  "relevance_score": 0.9,
  "chapter_section": "2_4_explainable_artificial_intelligence",
  "key_source_sentence": "SHAP values revealed that cutting speed contributed most to wear prediction accuracy."
}
```

### Output (evidence record inserted to SQLite + appended to JSON)
```json
{
  "id": 1,
  "thesis_sentence": "",
  "claim_type": "literature_evidence",
  "chapter_path": "ch02/2_4_explainable_artificial_intelligence",
  "source_paper_id": 317,
  "bibtex_key": "paper_317",
  "extracted_sentence": "SHAP values revealed that cutting speed contributed most to wear prediction accuracy.",
  "support_relation": "supports",
  "confidence": 0.9,
  "audit_status": "pending_bibtex"
}
```

---

## Example 2: Writing a paragraph from evidence

### Writing package (input to writing agent)
```
# Writing Package: Section 2.4 — Explainable AI
## Batch 1 of 4 (papers 1–5)

### Paper 317 — [paper_317]
Title: SHAP-based Interpretability for Predictive Maintenance
Year: 2024 | Relevance: 0.9
Key sentence: "SHAP values revealed that cutting speed contributed most to wear prediction accuracy."

### Paper 89 — [paper_89]
Title: LIME Explanations for Bearing Fault Diagnosis
Year: 2023 | Relevance: 0.85
Key sentence: "LIME-generated explanations highlighted frequency-domain features as primary fault indicators."

## Instructions
Write 1–2 paragraphs for Section 2.4 synthesising these papers.
Use \parencite{paper_317} style. Do not invent content.
```

### Output LaTeX paragraph
```latex
% writing/ch02_literature_review/s004_explainable_ai/p001/paragraph.tex
Explainable artificial intelligence (XAI) methods have been increasingly applied to predictive
maintenance models to provide human-interpretable justifications for failure predictions.
Among these, SHAP (SHapley Additive exPlanations) has demonstrated particular utility:
\textcite{paper_317} found that SHAP values revealed cutting speed as the dominant contributor
to wear prediction accuracy across multiple classifier types. Similarly, LIME-based explanations
have been applied to bearing fault diagnosis, with \textcite{paper_89} reporting that
frequency-domain features were consistently highlighted as primary fault indicators.
```

---

## Example 3: Wrong citation key (before vs after BibTeX audit)

### Before BibTeX audit (correct)
```latex
\parencite{paper_317}
```
`audit_status = "pending_bibtex"` — placeholder, safe to use in draft.

### After BibTeX generated (audited)
```latex
\parencite{Zhang2024}   % paper_317 → Zhang2024 confirmed in references.bib
```
`audit_status = "verified"` — key confirmed present in `.bib` file.

### What NOT to do
```latex
\parencite{Zhang_2024}   % ← invented key — paper_317 might be authored by someone else
```
Never guess real author-year keys. Always wait for BibTeX generation.

---

## Example 4: Evidence-first guard

### Wrong
```python
# Writing Section 2.3 without checking evidence exists
write_section("2_3_machine_learning_for_failure_classification")
# Results in empty paragraphs or invented content
```

### Correct
```python
count = db.execute(
    "SELECT COUNT(*) FROM thesis_sentence_evidence WHERE chapter_path LIKE '%%2_3%%'"
).fetchone()[0]
if count == 0:
    print("No evidence records for 2_3 — run Stage 8 first")
    sys.exit(1)
write_section("2_3_machine_learning_for_failure_classification")
```
