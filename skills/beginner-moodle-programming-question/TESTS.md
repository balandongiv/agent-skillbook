# Test Prompts: Beginner Moodle Programming Question

These prompts should trigger this skill when entered into an AI agent that has this skill loaded.

---

## Test Prompt 1

> "Create a beginner Moodle programming question about adding two integers. Use tags python, arithmetic, and input-output."

Expected behavior: The agent generates a complete beginner Moodle question with those tags, a partial answer preload, automatic test cases, and general feedback about common beginner mistakes.

---

## Test Prompt 2

> "Make a Moodle coding question for new students about checking if a number is positive, negative, or zero."

Expected behavior: The agent asks which tags should be used before generating the final question.

---

## Test Prompt 3

> "Write a beginner programming question for Moodle about counting from 1 to n, and include starter code but not the answer."

Expected behavior: The agent asks for tags if none are supplied, then creates a loop-based beginner task with scaffold comments, test cases, and feedback mentioning off-by-one and indentation errors.

---

## Test Prompt 4

> "Generate a simple Moodle exercise on string length for Python beginners with tags python, strings, and beginner."

Expected behavior: The agent creates a Python-based question, includes those tags, provides an incomplete starter template, and adds test cases that cover normal and edge input.

---

## Test Prompt 5

> "Using this Moodle XML template, create a CodeRunner question that gives marks separately for the first and second printed output lines."

Expected behavior: The agent keeps the XML format, uses a proper combinator `TemplateGrader` for partial marking across output lines, and does not rely on a single exact-match expected output block.
