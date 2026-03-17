#!/usr/bin/env python3
"""Build the full skill catalog by running all renderers for all skills."""
import subprocess
import sys
from pathlib import Path

SKILLS_DIR = Path(__file__).parent.parent / "skills"
TOOLS_DIR = Path(__file__).parent


def run_renderer(script: Path, skill_dir: Path) -> bool:
    """Run a single renderer script for a skill. Returns True on success."""
    result = subprocess.run(
        [sys.executable, str(script), str(skill_dir)],
        capture_output=True,
        text=True,
    )
    if result.stdout:
        print(result.stdout.rstrip())
    if result.returncode != 0:
        print(f"  ERROR: {result.stderr.strip()}", file=sys.stderr)
        return False
    return True


def main():
    if not SKILLS_DIR.exists():
        print("No skills/ directory found.")
        sys.exit(0)

    skill_dirs = sorted([d for d in SKILLS_DIR.iterdir() if d.is_dir() and not d.name.startswith(".")])
    if not skill_dirs:
        print("No skills found.")
        sys.exit(0)

    renderers = [
        TOOLS_DIR / "render_openai_skill.py",
        TOOLS_DIR / "render_claude_skill.py",
        TOOLS_DIR / "render_gemini_gem.py",
    ]

    total = 0
    failed = 0

    print(f"Building catalog for {len(skill_dirs)} skill(s)...\n")

    for skill_dir in skill_dirs:
        print(f"[{skill_dir.name}]")
        for renderer in renderers:
            success = run_renderer(renderer, skill_dir)
            total += 1
            if not success:
                failed += 1

    print(f"\nDone. {total - failed}/{total} renderers succeeded.")
    if failed:
        print(f"{failed} renderer(s) failed. See errors above.")
        sys.exit(1)
    else:
        print("Catalog build complete.")


if __name__ == "__main__":
    main()
