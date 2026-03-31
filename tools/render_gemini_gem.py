#!/usr/bin/env python3
"""Render the Gemini Gem export for a skill.

Usage:
    python render_gemini_gem.py <skill_dir> [output_dir]

If output_dir is not provided, writes to <skill_dir>/exports/gemini/.
"""
import sys
from pathlib import Path


def render_gemini_gem(skill_dir: Path, output_dir: Path) -> None:
    """Read canonical skill files and write Gemini Gem exports."""
    yaml_path = skill_dir / "skill.yaml"
    instructions_path = skill_dir / "INSTRUCTIONS.md"

    if not yaml_path.exists():
        print(f"Error: skill.yaml not found in {skill_dir}", file=sys.stderr)
        sys.exit(1)

    import yaml

    with open(yaml_path) as f:
        data = yaml.safe_load(f)

    slug = data.get("slug", skill_dir.name)
    title = data.get("title", slug)
    description = data.get("summary", "")
    when_to_use = data.get("when_to_use", [])
    when_not_to_use = data.get("when_not_to_use", [])

    instructions_content = ""
    if instructions_path.exists():
        instructions_content = instructions_path.read_text()

    when_to_use_lines = "\n".join(f"- {item}" for item in when_to_use)
    when_not_to_use_lines = "\n".join(f"- {item}" for item in when_not_to_use)

    output_dir.mkdir(parents=True, exist_ok=True)

    # Write GEM_INSTRUCTIONS.md
    gem_instructions = output_dir / "GEM_INSTRUCTIONS.md"
    gem_instructions.write_text(
        f"# Gem Instructions: {title}\n\n"
        f"<!-- Paste the content below into the Gemini Gem instructions field. -->\n\n"
        f"---\n\n"
        f"You are an expert assistant specialized in {title.lower()}.\n\n"
        f"## Your role\n\n"
        f"{description}\n\n"
        f"## Instructions\n\n"
        f"{instructions_content}\n"
        f"## When to apply these instructions\n\n"
        f"Apply these instructions when the user:\n\n"
        f"{when_to_use_lines}\n\n"
        f"Do not apply when:\n\n"
        f"{when_not_to_use_lines}\n"
    )

    # Write SETUP.md
    setup_md = output_dir / "SETUP.md"
    test_prompts_section = ""
    tests_path = skill_dir / "TESTS.md"
    if tests_path.exists():
        test_prompts_section = (
            "\n### Step 7: Test your Gem\n\n"
            "Open your new Gem and try a few of the test prompts from "
            f"`skills/{slug}/TESTS.md` to verify it is working correctly.\n"
        )

    setup_md.write_text(
        f"# Gemini Gem Setup Guide: {title}\n\n"
        f"This guide walks you through creating a Gemini Gem for this skill.\n\n"
        f"**Note:** Gemini Gems must be created manually through the Gemini web UI. "
        f"This repository cannot auto-register Gems.\n\n"
        f"---\n\n"
        f"## Prerequisites\n\n"
        f"- A Google account with access to [gemini.google.com](https://gemini.google.com)\n"
        f"- The `GEM_INSTRUCTIONS.md` file from this directory\n\n"
        f"---\n\n"
        f"## Step-by-step setup\n\n"
        f"### Step 1: Open Gemini\n\n"
        f"Go to [gemini.google.com](https://gemini.google.com) and sign in.\n\n"
        f"### Step 2: Navigate to Gems\n\n"
        f"In the left sidebar, click **Gems**.\n\n"
        f"### Step 3: Create a new Gem\n\n"
        f'Click the **New gem** button or the "+" icon.\n\n'
        f"### Step 4: Name your Gem\n\n"
        f"Enter the name: **{title}**\n\n"
        f"### Step 5: Add instructions\n\n"
        f"Open `GEM_INSTRUCTIONS.md` from this directory. "
        f"Copy the full content (after the HTML comment lines) and paste it into "
        f"the instructions field.\n\n"
        f"### Step 6: Save\n\n"
        f"Click **Save** to create the Gem."
        f"{test_prompts_section}\n\n"
        f"---\n\n"
        f"## Using the Gem\n\n"
        f"1. Go to [gemini.google.com](https://gemini.google.com)\n"
        f"2. Click **Gems** in the sidebar\n"
        f"3. Select **{title}**\n"
        f"4. Start your conversation\n\n"
        f"**Remember:** Select the Gem before asking your question. "
        f"Gemini requires manual Gem selection — it does not auto-route based on message content.\n\n"
        f"---\n\n"
        f"## Updating the Gem\n\n"
        f"When this skill is updated:\n\n"
        f"1. Regenerate: `python tools/render_gemini_gem.py skills/{slug}`\n"
        f"2. Open the updated `GEM_INSTRUCTIONS.md`\n"
        f"3. Edit your Gem in the Gemini UI and replace the instructions\n"
        f"4. Click **Save**\n"
    )

    print(f"Rendered Gemini export for '{slug}' -> {output_dir}")


def main():
    if len(sys.argv) < 2:
        print("Usage: render_gemini_gem.py <skill_dir> [output_dir]")
        sys.exit(1)

    skill_dir = Path(sys.argv[1])
    if len(sys.argv) >= 3:
        output_dir = Path(sys.argv[2])
    else:
        output_dir = skill_dir / "exports" / "gemini"

    render_gemini_gem(skill_dir, output_dir)


if __name__ == "__main__":
    main()
