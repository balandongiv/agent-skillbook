# Test Prompts: Creating a Python Class and Choosing the Right Python Filename

These prompts should trigger this skill when entered into an AI agent that has this skill loaded.
Use them to verify that the skill is correctly configured and that the routing description matches real class-naming requests.

---

## Test Prompt 1

> "I need to add a new Python class for loading blink annotations. What should I name the file and class?"

Expected behavior: The agent recommends a responsibility-based class and filename pairing such as `BlinkAnnotationLoader` in `blink_annotation_loader.py`, and explains the `PascalCase` / `snake_case` convention.

---

## Test Prompt 2

> "This file is called utils.py but it only contains class PathResolver. Should I rename it?"

Expected behavior: The agent advises renaming the module to `path_resolver.py`, explains why generic filenames are harder to search and debug, and keeps the class name as `PathResolver`.

---

## Test Prompt 3

> "Should this Python code be a class or just functions? It only filters filenames and stores no state."

Expected behavior: The agent recommends a function-oriented module instead of a class, explains that classes are better when state or lifecycle matters, and suggests a clear filename such as `filename_filters.py`.

---

## Test Prompt 4

> "I wrote class EARSignalProcessor. What should the Python filename be?"

Expected behavior: The agent converts the class name to a readable snake_case filename, recommends `ear_signal_processor.py`, and explains why abbreviations should stay readable.

---

## Test Prompt 5

> "Review this Python module naming: processing.py contains PathResolver, BlinkEvaluator, and SubjectRouter."

Expected behavior: The agent identifies the mixed responsibilities, recommends splitting the classes into separate files such as `path_resolver.py`, `blink_evaluator.py`, and `subject_router.py`, and explains the one-main-class-per-file default.

