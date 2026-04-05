# Example Uses: Beginner Moodle Programming Question

These examples show the kinds of requests that should trigger this skill.

---

## Example 1

User request:

> Create a Moodle programming question for beginners about calculating the area of a rectangle. Use tags `python`, `input-output`, and `arithmetic`.

Expected behavior:

- Generate a beginner-friendly question.
- Include the supplied tags.
- Include an answer preload with comments and no full solution.
- Include test cases automatically.
- Include general feedback about likely beginner mistakes such as forgetting numeric conversion or printing the wrong value.

---

## Example 2

User request:

> Make me a beginner Moodle coding question about checking whether a number is even or odd.

Expected behavior:

- Ask a follow-up question for tags before generating the question.
- After tags are provided, generate the full Moodle-ready question.

---

## Example 3

User request:

> Write a simple Moodle programming question on loops for first-semester students. I want starter code but not the full answer.

Expected behavior:

- Keep the loop task small and concrete.
- Provide starter code with comments such as `# Write your code here`.
- Avoid solving the exercise in the preload.
- Include test cases and beginner-focused general feedback.

---

## Example 4

User request:

> Create a Moodle XML CodeRunner question where the first printed line and second printed line should receive marks separately.

Expected behavior:

- Preserve the Moodle XML structure requested by the user.
- Avoid a plain exact-match whole-output grader.
- Use a proper combinator `TemplateGrader` when separate output components need separate marks.
- Return a result table that shows each graded component clearly.
