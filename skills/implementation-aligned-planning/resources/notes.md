# Notes: Implementation-Aligned Planning

## Research notes

This skill captures a documentation style that treats planning files as working engineering artifacts. The strongest recurring pattern is to convert broad plans into explicit contracts that can be checked against code and used during debugging.

The most important design move is separating intent from implementation truth. Plans often contain useful intent even when their concrete details are stale. The skill preserves intent where it helps, but updates concrete paths, outputs, and execution order to match the current codebase.

The second recurring pattern is that a stage plan becomes much more useful when it is also a navigation guide. Real module paths, real function names, read/write contracts, failure modes, and pseudocode are what turn a plan into an operational document.

## Open questions

- Should we add a companion skill focused specifically on folder-structure and flowchart synchronization across large repos?
- Should we standardize a shorter variant of the stage-doc structure for smaller utilities and one-file scripts?
