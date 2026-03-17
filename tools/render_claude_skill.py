#!/usr/bin/env python3
"""Render the Claude export for a skill.

Usage:
    python render_claude_skill.py <skill_dir> [output_dir]

If output_dir is not provided, writes to <skill_dir>/exports/claude/.
"""
import sys
from pathlib import Path


def render_claude_skill(skill_dir: Path, output_dir: Path) -> None:
    """Read canonical skill files and write Claude exports."""
    yaml_path = skill_dir / "skill.yaml"
    instructions_path = skill_dir / "INSTRUCTIONS.md"

    if not yaml_path.exists():
        print(f"Error: skill.yaml not found in {skill_dir}", file=sys.stderr)
        sys.exit(1)

    import yaml

    with open(yaml_path) as f:
        data = yaml.safe_load(f)

    slug = data.get("slug", skill_dir.name)
    description = data.get("summary", "")
    platform = data.get("platform_overrides", {}).get("claude", {})

    disable_model_invocation = platform.get("disable_model_invocation", False)
    user_invocable = platform.get("user_invocable", True)
    allowed_tools = platform.get("allowed_tools", [])
    allowed_tools_str = str(allowed_tools)  # e.g. "[]"

    instructions_content = ""
    if instructions_path.exists():
        instructions_content = instructions_path.read_text()

    output_dir.mkdir(parents=True, exist_ok=True)
    skill_md = output_dir / "SKILL.md"
    skill_md.write_text(
        f"---\n"
        f"name: {slug}\n"
        f"description: {description}\n"
        f"disable-model-invocation: {str(disable_model_invocation).lower()}\n"
        f"user-invocable: {str(user_invocable).lower()}\n"
        f"allowed-tools: {allowed_tools_str}\n"
        f"---\n\n"
        f"{instructions_content}"
    )

    print(f"Rendered Claude export for '{slug}' -> {output_dir}")


def main():
    if len(sys.argv) < 2:
        print("Usage: render_claude_skill.py <skill_dir> [output_dir]")
        sys.exit(1)

    skill_dir = Path(sys.argv[1])
    if len(sys.argv) >= 3:
        output_dir = Path(sys.argv[2])
    else:
        output_dir = skill_dir / "exports" / "claude"

    render_claude_skill(skill_dir, output_dir)


if __name__ == "__main__":
    main()
