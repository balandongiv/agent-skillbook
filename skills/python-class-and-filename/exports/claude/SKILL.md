---
name: python-class-and-filename
description: Create focused Python classes and choose matching snake_case module filenames when adding or refactoring class-based code.
disable-model-invocation: false
user-invocable: true
allowed-tools: []
---

# Creating a Python Class and Choosing the Right Python Filename

This skill defines a practical standard for creating Python classes and naming the `.py` file that contains them. Use it when you are adding a new class, refactoring a generic module into a clearer one, or deciding whether a file should center around a class at all.

The goal is to make Python code easy to find, easy to import, easy to debug, and consistent across the repository. The core rule is simple: the filename should describe the module responsibility, and the class name should describe the object responsibility.

---

## Core principles

### 1. Use `snake_case` filenames and `PascalCase` class names

Pair module names and class names predictably.

```python
# file: path_resolver.py
class PathResolver:
    pass
```

### 2. Name the file after the main concept inside it

If a file contains one important class, name the file after that class converted to `snake_case`.

Examples:

- `PathResolver` → `path_resolver.py`
- `BlinkAnnotationLoader` → `blink_annotation_loader.py`
- `EARSignalProcessor` → `ear_signal_processor.py`
- `ExperimentConfig` → `experiment_config.py`

Avoid vague filenames like `utils.py`, `helpers.py`, `common.py`, or `misc.py` when the file really has one clear responsibility.

### 3. Use one main class per file by default

The safest default is one main class per file, with the filename matching that class concept. This improves IDE navigation, imports, stack traces, and code search.

Small helper dataclasses, enums, or tightly coupled private helpers may live in the same file when they only support the main class.

### 4. Choose names based on responsibility

The filename should tell a reader what the module is for.

- data access: `ear_data_loader.py`
- path handling: `path_resolver.py`
- processing: `blink_signal_processor.py`
- configuration: `experiment_config.py`
- evaluation: `blink_evaluator.py`

Choose names that reflect the real job of the class instead of broad placeholder names.

### 5. Do not force a class when a function module is the better fit

Use a class when state must be stored across methods, configuration belongs to the object, or multiple related operations act on the same object. Use a function module when the logic is stateless, small, and reusable.

```python
# file: path_utils.py

def normalize_path(path: str) -> str:
    ...


def ensure_dir(path: str) -> None:
    ...
```

A file like this should stay function-oriented unless there is a real object abstraction to model.

### 6. Keep constructors focused

Constructors should only receive the dependencies the class needs. If `__init__` takes many unrelated arguments, the class may have too many responsibilities.

```python
from pathlib import Path


class EARDataLoader:
    def __init__(self, data_root: Path) -> None:
        self.data_root = Path(data_root)
```

---

## Step-by-step process

When creating or reviewing a Python class and its filename:

1. Identify the module's main responsibility.
2. Decide whether the code truly needs object state or lifecycle.
3. If it does, name the class in `PascalCase` using a noun or noun phrase that describes the object.
4. Convert that class name into a clear `snake_case.py` filename.
5. Check that the import reads naturally.
6. Confirm there is one clear main class in the file.
7. Rename vague modules to specific responsibility-based names when needed.

A good import should feel obvious:

```python
from src.preprocessing.path_resolver import PathResolver
from src.annotation.blink_annotation_loader import BlinkAnnotationLoader
from src.experiments.experiment_runner import ExperimentRunner
```

If the import feels awkward or overly generic, rename the file or class.

---

## Rules

- Use `PascalCase` for Python class names.
- Use `snake_case.py` for Python filenames.
- Match the filename to the main class concept when the file has one main class.
- Prefer one main class per file.
- Prefer responsibility-based names over generic names.
- Keep abbreviations readable: `csv_annotation_loader.py` is better than `csvloader.py`.
- Use a function module instead of a class when there is no real object state to manage.

---

## Common mistakes to avoid

- **Generic filenames**: `utils.py`, `stuff.py`, `temp.py`, `common.py`. These make search and debugging harder.
- **Mismatch between file and class**: a file named `processing.py` that only contains `PathResolver` is misleading.
- **Too many unrelated classes in one file**: combining `PathResolver`, `BlinkEvaluator`, and `SubjectRouter` in one module hides responsibility.
- **Overcompressed names**: `earsigproc.py` is much harder to read than `ear_signal_processor.py`.
- **Unnecessary classes**: wrapping small stateless helpers in a class without state adds indirection and worse imports.

---

## Additional guidance

Use this minimal pattern as a default for new class files:

```python
"""Short module description."""

from __future__ import annotations

from pathlib import Path


class PathResolver:
    """Resolve important project paths from a base directory."""

    def __init__(self, root_dir: Path) -> None:
        self.root_dir = Path(root_dir)

    def get_data_dir(self) -> Path:
        return self.root_dir / "data"
```

Suggested filename: `path_resolver.py`

Before finalizing a class and filename, ask:

1. What is the main responsibility?
2. Is this really a class, or should it be functions?
3. Is there one clear main class in the file?
4. Does the filename describe the module clearly?
5. Does the class name describe the object clearly?
6. Does the import read naturally?
7. Will another developer find it quickly by search?

