# Notes: IntelliJ Line Debugging

## Research notes

This skill encodes a debugging style centered on human traceability rather than raw throughput. The key pattern is to turn broad, parallel, cache-heavy production flows into a smallest-real-scope serial path that still calls the real production functions.

The most reusable insight is that debugging becomes much easier when the helper and the production stage share the same call order. A good helper is not an alternate implementation. It is a guided entrance into the real one.

The second recurring pattern is that breakpoint quality matters more than breakpoint count. Users benefit more from an explicit breakpoint order than from being told to "explore the file."

## Open questions

- Should this skill grow a short reference section for common IntelliJ debugger settings by language or framework?
- Should we add a companion skill specifically for debugging data alignment, joins, and off-by-one boundaries?
