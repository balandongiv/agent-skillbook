#!/usr/bin/env python3
"""List all canonical skills in the skills/ directory."""
import sys
from pathlib import Path

SKILLS_DIR = Path(__file__).parent.parent / "skills"


def list_skills():
    if not SKILLS_DIR.exists():
        print("No skills/ directory found.")
        return
    skills = sorted([d for d in SKILLS_DIR.iterdir() if d.is_dir()])
    if not skills:
        print("No skills found.")
        return
    print(f"Found {len(skills)} skill(s):\n")
    for skill_dir in skills:
        yaml_path = skill_dir / "skill.yaml"
        if yaml_path.exists():
            try:
                import yaml
                with open(yaml_path) as f:
                    data = yaml.safe_load(f)
                title = data.get("title", skill_dir.name)
                summary = data.get("summary", "")
                print(f"  {skill_dir.name}")
                print(f"    Title:   {title}")
                print(f"    Summary: {summary}")
                print()
            except Exception as e:
                print(f"  {skill_dir.name} (error reading skill.yaml: {e})")
        else:
            print(f"  {skill_dir.name} (no skill.yaml)")


if __name__ == "__main__":
    list_skills()
