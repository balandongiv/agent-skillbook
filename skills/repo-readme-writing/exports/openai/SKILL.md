---
name: repo-readme-writing
description: Write clear, structured, beginner-friendly README files for GitHub repositories that explain purpose, setup, and usage.
---

# Repo README Writing

This skill guides you through writing a README file that serves as the front door to a GitHub repository. A great README makes a project accessible to newcomers, explains the project's purpose clearly, and helps users get started quickly. Apply this skill when creating a new README or substantially revising an existing one.

---

## Core principles

### 1. Write for a beginner audience (unless told otherwise)

Assume the reader has never seen your project before. They may be:
- A developer evaluating whether to use your library
- A contributor looking to understand the codebase
- A student learning from your code
- You, six months from now, having forgotten how everything works

Write as if you are explaining to someone who is intelligent but unfamiliar with your specific project, tools, or conventions.

### 2. Start with what and why

The very first paragraph should answer two questions:
1. **What is this project?** (One sentence. No jargon.)
2. **Why does it exist? What problem does it solve?**

A reader should be able to decide in 15 seconds whether this project is relevant to them.

### 3. Include a Quick Start section early

Put the minimal working example as early as possible. Don't make the reader scroll through architecture diagrams and feature lists to find out how to install and run the project.

A quick start should have the user running something in under 5 minutes.

### 4. Document every installation step explicitly

Never assume a step is obvious. Explicitly document:
- System requirements (Python version, OS, etc.)
- How to clone the repository
- How to install dependencies
- How to run a basic example

### 5. Show usage with real examples

Code examples are the most valuable part of a README for a developer audience. Show real, runnable code — not pseudocode or placeholders.

### 6. Use clear, scannable headings

Readers scan before they read. Use ATX-style headings (`##` not underline style) with meaningful names:
- `## Installation`
- `## Quick Start`
- `## Usage`
- `## Contributing`
- `## License`

Avoid creative heading names like "Getting Your Hands Dirty" — they slow down scanning.

### 7. Link to detailed docs

The README is a front door, not an encyclopedia. For complex topics, write a brief intro in the README and link to a more detailed doc. Keep the README under 500 lines if possible.

### 8. Keep it up to date

A README that describes version 0.1 behavior for a 2.0 project is worse than no README. Update the README as part of any major feature change.

---

## Required sections for most projects

1. **Title and one-line description** — What is this?
2. **Why it exists** — What problem does it solve?
3. **Quick Start** — How to install and run in under 5 minutes
4. **Installation** — Detailed installation steps
5. **Usage** — How to use it, with examples
6. **Configuration** (if applicable) — Key configuration options
7. **Contributing** — How to contribute (or link to CONTRIBUTING.md)
8. **License** — License type and link

Optional but recommended:
- **Badges** — CI status, version, license (keep to 3-5 maximum)
- **Roadmap** or **Status** — Is this production-ready? Experimental?
- **FAQ** — Common questions and gotchas
- **Acknowledgements** — Dependencies, inspiration, contributors

---

## Step-by-step writing process

1. **Start with the title and one-sentence description.** Write it last if needed — but put it first.
2. **Write the Quick Start section.** This forces you to know the minimal path.
3. **Write Installation with every step explicit.** Test it on a clean environment if possible.
4. **Write Usage with the three most common use cases.**
5. **Add Contributing guidance** — even a one-liner ("Open an issue or submit a PR") is better than nothing.
6. **Add License.**
7. **Review for jargon.** Replace every unexplained acronym or term with a brief explanation.
8. **Read the first paragraph aloud.** Does it make sense to someone who has never heard of this project?

---

## Common mistakes to avoid

- **Starting with installation before explaining what the project is.** Installation without motivation is confusing.
- **Assuming familiarity with dependencies.** Link to installation pages for every non-trivial dependency.
- **Outdated examples.** Always test your code examples before publishing.
- **Missing license information.** An open source project without a license is legally ambiguous.
- **Walls of text.** Use lists, code blocks, and headings to break up content.
- **Too many badges.** More than 5-6 badges becomes visual noise.
