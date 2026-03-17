# Notes: Good Function Design

## References

- [Clean Code by Robert C. Martin](https://www.oreilly.com/library/view/clean-code-a/9780136083238/) — Chapter 3 covers function design principles in depth.
- [Python documentation: Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [PEP 257 – Docstring Conventions](https://peps.python.org/pep-0257/)
- [PEP 484 – Type Hints](https://peps.python.org/pep-0484/)

## Research notes

The "20 lines" rule is a guideline, not a hard limit. The real principle is single responsibility. A 25-line function that does one thing clearly is better than a 15-line function that does two things.

The mutable default argument antipattern is a well-known Python gotcha. It has caused production bugs in many codebases. Worth calling out explicitly.

Pure functions are highly valued in functional programming, but even in object-oriented Python they are a useful goal. The test "could this function be a static method?" is a useful proxy for purity.

## Open questions

- Should we include guidance on `@staticmethod` vs `@classmethod`?
- Should we address generator functions (functions with `yield`) separately?
