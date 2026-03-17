# Notes: Creating a Python Class and Choosing the Right Python Filename

## References

- [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [The Python Tutorial – Classes](https://docs.python.org/3/tutorial/classes.html)
- [Python Packaging User Guide](https://packaging.python.org/)

## Research notes

This skill focuses on day-to-day module naming inside Python projects rather than full package architecture. The most important practical rule is that the filename should describe the module responsibility while the class name describes the object responsibility.

The guidance intentionally keeps the default simple: one main class per file, `PascalCase` for classes, `snake_case.py` for filenames, and responsibility-based names that read naturally in imports.

A second important boundary in this skill is deciding when not to introduce a class. Stateless helpers often read better as function modules, so the instructions explicitly distinguish object-oriented code from function-oriented modules.

## Open questions

- Should a future companion skill cover package naming and `__init__.py` export conventions?
- Should this skill eventually include framework-specific examples for Django, FastAPI, or PyTorch projects?

