# Notes: Good Description Writing

## References

- [OpenAI Function Calling Guide](https://platform.openai.com/docs/guides/function-calling) — explains how OpenAI uses descriptions to route tool calls.
- [Anthropic Tool Use Documentation](https://docs.anthropic.com/en/docs/tool-use) — explains how Claude uses descriptions to decide which tool to invoke.
- [Prompt Engineering Guide](https://www.promptingguide.ai/) — general reference on writing effective prompts.

## Research notes

The routing problem for agent skills is analogous to the problem of writing good search engine meta descriptions — except the "search engine" is a language model rather than a keyword matcher. The key insight is that language models use semantic similarity, so filler words that are semantically generic ("handles", "manages") add noise without discriminative signal.

Empirically, descriptions that include specific nouns (the type of artifact being produced) and specific verbs (the action being taken) outperform generic descriptions in routing accuracy.

## Open questions

- How much does description length affect matching quality? Is there an optimal length?
- Should descriptions be written in the imperative ("Write X") or declarative ("Writes X") form?
