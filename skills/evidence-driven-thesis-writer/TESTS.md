# Tests — Evidence-Driven Thesis Writer

## T1: Evidence guard blocks writing with zero records

**Given** `thesis_sentence_evidence` has 0 records for `chapter_path LIKE '%2_3%'`  
**When** `write_section("2_3_machine_learning_for_failure_classification")` is called  
**Then** the function exits with an error message and no `.tex` files are written

**Verify**: No `p001/paragraph.tex` created under `s003_machine_learning/` directory.

---

## T2: Placeholder bibtex key format

**Given** `paper_id = 317`  
**When** an evidence record is created  
**Then** `bibtex_key = "paper_317"` and `audit_status = "pending_bibtex"`

**Verify**: No `_` or `-` in the numeric part; format is exactly `paper_{int(paper_id)}`.

---

## T3: No target-label columns in evidence claims

**Given** evidence records for any chapter section  
**When** all `extracted_sentence` and `thesis_sentence` values are scanned  
**Then** none contain the strings: "Machine failure", "TWF", "HDF", "PWF", "OSF", "RNF" as input features

**Verify**: Regex `\b(TWF|HDF|PWF|OSF|RNF)\b.*(?:input|feature|predictor)` matches nothing.

---

## T4: Evidence JSON saved per section AND combined

**Given** 387 include papers are assigned to 5 different `chapter_section` values  
**When** Stage 8 (build evidence JSON) completes  
**Then** 5 section-specific JSON files AND 1 `evidence_all.json` exist in `evidence/`

**Verify**: `glob("evidence/evidence_*.json")` returns 6 files.

---

## T5: Paragraph file follows LATEX_STRUCTURE_REQUIREMENTS

**Given** evidence is available for Section 2.4 with 8 papers  
**When** paragraphs are written  
**Then** each paragraph is in its own `p###/paragraph.tex` (no prose in `section.tex`)

**Verify**: `writing/ch02_literature_review/s004_*/section.tex` contains only `\section{}` and `\input{}` lines.

---

## T6: BibTeX audit updates status

**Given** `paper_317` appears in `references.bib` as key `Zhang2024`  
**When** `audit_bibtex("paper_317", "Zhang2024")` is called  
**Then** `audit_status` is updated to `"verified"` and `bibtex_key` updated to `"Zhang2024"`

**Verify**: SQLite query `SELECT bibtex_key, audit_status WHERE source_paper_id=317` returns `("Zhang2024", "verified")`.

---

## T7: Writing package batch size respected

**Given** 40 include papers assigned to Section 2.3  
**When** writing packages are exported  
**Then** 2 packages are created (20 papers each), and no paper appears in both packages

**Verify**: No `paper_id` duplicated across `writing_package_2_3_batch_1.md` and `writing_package_2_3_batch_2.md`.
