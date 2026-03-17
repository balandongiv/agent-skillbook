# Test Prompts: Good Function Design

These prompts should trigger this skill when entered into an AI agent that has this skill loaded.

---

## Test Prompt 1

> "Write a function to process and save user data"

Expected behavior: The agent applies the good-function-design skill and writes separate small functions — one to process, one to save — with explicit parameters and type hints.

---

## Test Prompt 2

> "This function is 80 lines long, help me refactor it"

Expected behavior: The agent identifies multiple responsibilities in the function and proposes extracting each into a smaller, named function.

---

## Test Prompt 3

> "How should I name this Python function?"

Expected behavior: The agent advises using a verb-phrase name that describes the action and the subject clearly, and gives concrete examples of good vs poor names.

---

## Test Prompt 4

> "Review this function for testability"

Expected behavior: The agent checks for hidden state, side effects, multiple responsibilities, and missing type hints. It suggests concrete changes to make the function easier to unit test.

---

## Test Prompt 5

> "What should a Python function return?"

Expected behavior: The agent explains that functions should have explicit return values with type annotations, avoid implicit `None` returns, and use `Optional[T]` when None is a valid result.
