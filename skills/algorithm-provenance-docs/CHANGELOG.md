# Changelog: Algorithm Provenance Documentation

All notable changes to this skill are documented here.

## [Unreleased]

## [0.1.0] - 2026-07-21

### Added
- Initial version of algorithm-provenance-docs.
- Core instructions for a fixed per-algorithm integration report (`docs/algorithms/<name>.md`):
  mandatory provenance, hypothesis, method linked to the shared harness, pre-registered
  falsifiers, exploratory results with split/n/baseline/caveat, and how to select/run/test the
  algorithm independently — passing a future-agent test with no git archaeology.
- Examples covering a bare-code-drop to a full report, honest linked (not duplicated) results,
  and cross-checking the report against the registry.
- Test prompts for documenting one algorithm, consistent multi-algorithm write-ups, provenance
  capture, honest results, single-source linking, doc/code agreement, and the future-agent test.
