#!/usr/bin/env python3
"""Render the OpenAI export for a skill.

Usage:
    python render_openai_skill.py <skill_dir> [output_dir]

If output_dir is not provided, writes to <skill_dir>/exports/openai/.
"""
import sys
from pathlib import Path


def render_openai_skill(skill_dir: Path, output_dir: Path) -> None:
    """Read canonical skill files and write OpenAI exports."""
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

    instructions_content = ""
    if instructions_path.exists():
        instructions_content = instructions_path.read_text()

    # Write SKILL.md
    output_dir.mkdir(parents=True, exist_ok=True)
    skill_md = output_dir / "SKILL.md"
    skill_md.write_text(
        f"---\n"
        f"name: {slug}\n"
        f"description: {description}\n"
        f"---\n\n"
        f"{instructions_content}"
    )

    # Write agents/openai.yaml
    agents_dir = output_dir / "agents"
    agents_dir.mkdir(parents=True, exist_ok=True)
    openai_yaml = agents_dir / "openai.yaml"
    openai_yaml.write_text(
        f"name: {slug}\n"
        f"description: {description}\n"
        f"instructions_file: ../SKILL.md\n"
    )

    print(f"Rendered OpenAI export for '{slug}' -> {output_dir}")


def main():
    if len(sys.argv) < 2:
        print("Usage: render_openai_skill.py <skill_dir> [output_dir]")
        sys.exit(1)

    skill_dir = Path(sys.argv[1])
    if len(sys.argv) >= 3:
        output_dir = Path(sys.argv[2])
    else:
        output_dir = skill_dir / "exports" / "openai"

    render_openai_skill(skill_dir, output_dir)


if __name__ == "__main__":
    main()
