# Examples: Repo README Writing

---

## Example 1: Replacing a minimal README with a structured one

### Before (without this skill)

```markdown
# mylib

A Python library for data processing.

## Installation

pip install mylib

## Usage

See docs.
```

### After (with this skill applied)

```markdown
# mylib

**Fast, composable data processing pipelines for Python.**

mylib lets you build data transformation pipelines from small, reusable steps.
It is designed for data scientists who need reproducible, testable data workflows
without the overhead of a full ETL framework.

## Quick Start

```bash
pip install mylib
```

```python
from mylib import Pipeline, Step

pipeline = Pipeline([
    Step("clean", lambda df: df.dropna()),
    Step("normalize", lambda df: (df - df.mean()) / df.std()),
])

result = pipeline.run(my_dataframe)
```

## Installation

Requires Python 3.9+.

```bash
pip install mylib
```

For development:

```bash
git clone https://github.com/example/mylib.git
cd mylib
pip install -e ".[dev]"
```

## Usage

[real usage section with examples]

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT. See [LICENSE](LICENSE).
```

### Why it's better

The improved README answers "what is this?" in the first sentence, gives a runnable example within the first scroll, and includes actual installation steps. A developer evaluating the library can understand it and run it in under 2 minutes.

---

## Example 2: Rewriting a jargon-heavy README for a beginner audience

### Before (without this skill)

```markdown
# agent-router

A semantic dispatch layer with pluggable resolver backends for LLM agent orchestration.

## Setup

Ensure you have the required dependencies provisioned and configure your resolver
via the AGENT_ROUTER_CONFIG environment variable before invoking the dispatcher.
```

### After (with this skill applied)

```markdown
# agent-router

**Route AI agent requests to the right handler automatically.**

agent-router reads a user's message and decides which function or tool to call,
based on the descriptions you provide. It is built for Python applications that
use OpenAI, Anthropic, or similar AI APIs.

## Quick Start

```bash
pip install agent-router
```

```python
from agent_router import Router

router = Router()

@router.skill(description="Answer questions about the weather in a city")
def get_weather(city: str) -> str:
    return f"The weather in {city} is sunny."

response = router.dispatch("What is the weather in Paris?")
# Calls get_weather("Paris")
```

## Installation

Requires Python 3.9+ and an OpenAI API key.

1. Install the package:
   ```bash
   pip install agent-router
   ```

2. Set your API key:
   ```bash
   export OPENAI_API_KEY=your-key-here
   ```

3. Run the example above to verify it works.

## Configuration

[clear configuration section]
```

### Why it's better

The original README used jargon ("semantic dispatch layer", "pluggable resolver backends", "provisioned") without explaining any of it. A new user would have no idea how to start. The rewritten version uses plain English, includes a Quick Start with a complete working example, and explains what each setup step does.
