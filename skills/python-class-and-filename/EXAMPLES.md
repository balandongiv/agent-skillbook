# Examples: Creating a Python Class and Choosing the Right Python Filename

---

## Example 1: Renaming a generic module to match the class responsibility

### Before (without this skill)

```python
# file: utils.py
class BlinkDetector:
    def __init__(self, threshold: float) -> None:
        self.threshold = threshold

    def detect(self, signal: list[float]) -> bool:
        return min(signal) < self.threshold
```

### After (with this skill applied)

```python
# file: blink_detector.py
class BlinkDetector:
    def __init__(self, threshold: float) -> None:
        self.threshold = threshold

    def detect(self, signal: list[float]) -> bool:
        return min(signal) < self.threshold
```

### Why it's better

The class already has a clear responsibility, so the file should reflect it. `blink_detector.py` is easier to search for, easier to import, and clearer in stack traces than `utils.py`.

---

## Example 2: Choosing a class only when state belongs to the object

### Before (without this skill)

```python
# file: filename_helpers.py
class FilenameFilter:
    def filter_by_subject(self, paths: list[str], subject_id: str) -> list[str]:
        return [path for path in paths if subject_id in path]

    def filter_by_suffix(self, paths: list[str], suffix: str) -> list[str]:
        return [path for path in paths if path.endswith(suffix)]
```

### After (with this skill applied)

```python
# file: filename_filters.py

def filter_by_subject(paths: list[str], subject_id: str) -> list[str]:
    return [path for path in paths if subject_id in path]



def filter_by_suffix(paths: list[str], suffix: str) -> list[str]:
    return [path for path in paths if path.endswith(suffix)]
```

### Why it's better

These helpers are stateless and do not need object lifecycle or stored configuration. A function module is simpler than an unnecessary class, and the filename now describes the module responsibility directly.

---

## Example 3: Keeping one main class per file with a clean import

### Before (without this skill)

```python
# file: processing.py
class PathResolver:
    def __init__(self, root_dir: str) -> None:
        self.root_dir = root_dir


class BlinkEvaluator:
    def evaluate(self, predictions: list[int], labels: list[int]) -> float:
        return 0.0
```

### After (with this skill applied)

```python
# file: path_resolver.py
class PathResolver:
    def __init__(self, root_dir: str) -> None:
        self.root_dir = root_dir
```

```python
# file: blink_evaluator.py
class BlinkEvaluator:
    def evaluate(self, predictions: list[int], labels: list[int]) -> float:
        return 0.0
```

```python
from src.preprocessing.path_resolver import PathResolver
from src.evaluation.blink_evaluator import BlinkEvaluator
```

### Why it's better

Each module now has one clear responsibility. The filenames and imports tell the reader exactly where to look, and the codebase becomes easier to navigate and refactor.

