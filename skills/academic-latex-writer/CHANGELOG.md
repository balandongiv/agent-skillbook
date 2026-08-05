# Changelog: Academic LaTeX Paragraph Writer (ChatGPT UI)

All notable changes to this skill are documented here.

## [Unreleased]

### Changed
- No unreleased changes yet.

## [0.1.0] - 2026-08-04

### Added
- Initial skill: draft manuscript prose through the ChatGPT web UI one paragraph at a time,
  in LaTeX, with each paragraph in its own file.
- Mandatory topic-sentence contract with transitions carried in the opening sentence.
- Evidence-packet grounding: every permitted number is computed in code, never by the model.
- `resources/prose_gates.py` and `resources/paragraph_writer.py` shipping the working loop.
- Documented LaTeX silent-failure hazards introduced by the UI renderer and by shell heredocs.
