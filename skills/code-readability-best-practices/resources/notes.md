# Notes: Code Readability Best Practices

## References

- [The Art of Readable Code by Dustin Boswell and Trevor Foucher](https://www.oreilly.com/library/view/the-art-of/9781449318482/)
- [Refactoring by Martin Fowler](https://martinfowler.com/books/refactoring.html)
- [Code Complete by Steve McConnell](https://www.oreilly.com/library/view/code-complete-2nd/0735619670/)

## Research notes

This skill emphasizes file organization as a reading experience: headline first, supporting detail below, and low-level helpers further down. The strongest recurring pattern is top-down flow that lets a reviewer understand intent before implementation.

The comment guidance is intentionally strict. Most readability gains come from deleting or rewriting comments that are vague, stale, overlong, or full of markup. Comments should explain constraints, reasons, business rules, caveats, or precise future work.

The examples and rules in this skill were reconstructed from visible on-screen guidance in uploaded videos. They are designed to preserve the practical best-practice ideas shown there rather than reproduce a word-for-word transcript.

## Open questions

- Should this skill include language-specific guidance for Python docstrings versus inline comments?
- Should we add a companion skill focused on readability reviews for large multi-file changes?

