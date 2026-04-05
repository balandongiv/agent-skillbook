# Beginner Moodle Programming Question

Generate a Moodle-ready beginner programming question that is easy to attempt, easy to grade, and clear about what the student must write.

---

## Workflow

1. Check whether the user already provided tags.
2. If tags are missing, ask one concise follow-up question asking which tags should be used.
3. Once tags are available, generate the full question in one response.
4. If the user did not specify a programming language, default to Python and state that assumption.
5. Keep the difficulty at true beginner level unless the user explicitly asks for something harder.

---

## Output requirements

Produce the question with these sections in this order:

1. `Question name`
2. `Question text`
3. `Tags`
4. `Answer preload`
5. `Test cases`
6. `General feedback`

Use short, teacher-friendly labels and keep the wording ready to paste into Moodle.

---

## Question text rules

- Describe one small programming task only.
- Use simple verbs such as `print`, `read`, `calculate`, `compare`, `repeat`, or `return`.
- State the exact input and output expectations.
- Avoid multi-part requirements unless the user explicitly asks for them.
- Avoid hidden complexity such as file handling, classes, recursion, or advanced libraries for beginner questions.
- Prefer realistic but simple contexts such as marks, age, temperature, price, counting, or string formatting.

---

## Tags rules

- If the user did not provide tags, do not guess silently.
- Ask a direct question such as: `Which tags should I use for this Moodle question?`
- Once the user answers, include the tags exactly as given unless they are clearly malformed.
- If the user gives broad tags, keep them but you may add one or two precise programming tags only when they are obviously useful and consistent with the request.

---

## Answer preload rules

- Always include an `Answer preload` section.
- Never provide a complete working solution in the preload.
- Give the student a useful starting scaffold only.
- Include one or more beginner-friendly comments that clearly mark where the student should write code.
- Prefer comments such as:
  - `# Write your code here`
  - `# Read the input here`
  - `# Calculate the result here`
  - `# Print the answer here`
- The preload may include a function signature, variable names, or input placeholders, but it must not already solve the task.
- If the task is function-based, provide the function header and a placeholder body such as `pass` or a TODO comment.

Example preload shape:

```python
def solve():
    # Read the input here

    # Calculate the result here

    # Print the answer here

if __name__ == "__main__":
    solve()
```

---

## Test case rules

- Always create test cases automatically, even if the user does not request them.
- Provide enough cases to check the main path and common edge behavior for a beginner task.
- Prefer 3 to 5 test cases.
- Include at least:
  - one normal case
  - one boundary or small edge case
  - one case that exposes a common beginner mistake when appropriate
- Present each test case with clear `Input` and `Expected output`.
- Keep values small and readable unless the lesson objective needs something else.

---

## Moodle XML and partial-mark rules

- If the user asks for Moodle XML, follow the supplied template or export structure exactly.
- If the question only needs whole-answer grading, standard exact-output test cases are acceptable.
- If the user wants separate marks for separate outputs or components, do not rely on plain exact-output test cases alone.
- For CodeRunner XML that must award partial marks across multiple printed lines or sub-results, use a proper combinator `TemplateGrader`.
- In that situation, run the student program once, inspect the produced output, and build a result table with one row per graded component.
- Put the total fraction at the top-level JSON object and put per-component details inside `testresults`.
- Do not emit per-test fields like `got` as top-level JSON from a combinator grader.
- Avoid fragile grading designs that depend on optional XML fields being preserved on import unless the template definitely supports them.

---

## General feedback rules

- Always include `General feedback`.
- Focus on mistakes a new programming student is likely to make.
- Give correction-oriented guidance, not just generic encouragement.
- Mention likely failure modes such as:
  - forgetting to convert text input to numbers
  - printing extra words or punctuation
  - using the wrong arithmetic operator
  - confusing `=` with `==`
  - off-by-one mistakes in loops
  - incorrect indentation
  - returning a value when the task expects printed output, or the reverse
- Keep the feedback specific to the question topic.

---

## Quality bar

- Keep the problem solvable in a few lines.
- Make the required output unambiguous.
- Ensure the preload, test cases, and feedback all match the same task.
- Do not leak the complete solution in any section.
- If the user asks for a template or XML-like packaging later, reuse the same content and keep the partial preload intact.
