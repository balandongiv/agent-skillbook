# Test Prompts: Good Description Writing

---

## Test Prompt 1

> "Write a description for my agent skill that handles user authentication"

Expected behavior: The agent flags "handles" as a filler word and rewrites the description using a specific action verb, naming the exact operation and context.

---

## Test Prompt 2

> "My skill isn't triggering when it should — what's wrong with this description: 'Helps users with their code problems'"

Expected behavior: The agent diagnoses the vague description and rewrites it with a specific action verb, concrete output, and routing context.

---

## Test Prompt 3

> "How do I write the description field for an OpenAI tool definition?"

Expected behavior: The agent explains that the description is the routing trigger, applies the formula (verb + specific output + context), and gives a before/after example.

---

## Test Prompt 4

> "What makes a good skill summary in skill.yaml?"

Expected behavior: The agent applies the good-description-writing principles: start with a verb, name the specific output, include when it applies, avoid filler words.

---

## Test Prompt 5

> "This tool description is too vague: 'Manages file operations.' How should I rewrite it?"

Expected behavior: The agent rewrites the description with a specific action (read/write/delete), a specific file type or context, and the trigger condition.
