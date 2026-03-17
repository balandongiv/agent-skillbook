#!/usr/bin/env python3
"""Validate all canonical skills in the skills/ directory."""
import sys
from pathlib import Path

# Allow importing from src/ without installing
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from agent_skillbook.validators import validate_all_skills

SKILLS_DIR = Path(__file__).parent.parent / "skills"


def main():
    results = validate_all_skills(SKILLS_DIR)
    if not results:
        print("No skills found.")
        sys.exit(0)

    all_ok = True
    for name, result in results.items():
        if result["ok"]:
            print(f"  OK    {name}")
        else:
            all_ok = False
            print(f"  FAIL  {name}")
            for error in result["errors"]:
                print(f"        - {error}")

    print()
    if all_ok:
        print(f"All {len(results)} skill(s) valid.")
    else:
        failed = [n for n, r in results.items() if not r["ok"]]
        print(f"Validation FAILED for: {', '.join(failed)}")
        print("Fix the errors above, then re-run validation.")
        sys.exit(1)


if __name__ == "__main__":
    main()
