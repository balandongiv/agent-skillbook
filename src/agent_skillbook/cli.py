"""Command-line interface for agent_skillbook."""
import sys
from pathlib import Path

SKILLS_DIR = Path(__file__).parent.parent.parent / "skills"


def cmd_list(args):
    from .registry import list_skills
    skills = list_skills(SKILLS_DIR)
    if not skills:
        print("No skills found.")
        return
    print(f"Found {len(skills)} skill(s):\n")
    for skill in skills:
        print(f"  {skill.slug}")
        print(f"    Title:   {skill.title}")
        print(f"    Summary: {skill.summary}")
        if skill.tags:
            print(f"    Tags:    {', '.join(skill.tags)}")
        print()


def cmd_validate(args):
    from .validators import validate_all_skills, validate_repository_versioning
    results = validate_all_skills(SKILLS_DIR)
    repo_root = SKILLS_DIR.parent
    repo_ok, repo_errors = validate_repository_versioning(repo_root)

    if not results and repo_ok:
        print("No skills found.")
        return

    all_ok = True
    if repo_ok:
        print("  OK  repository-versioning")
    else:
        all_ok = False
        print("  FAIL  repository-versioning")
        for error in repo_errors:
            print(f"        - {error}")

    for name, result in results.items():
        if result["ok"]:
            print(f"  OK  {name}")
        else:
            all_ok = False
            print(f"  FAIL  {name}")
            for error in result["errors"]:
                print(f"        - {error}")
    print()
    if all_ok:
        print("All skills valid. Version metadata is consistent.")
        print("Reminder: record edits under the relevant [Unreleased] changelog section, and bump package versions together when cutting a release.")
    else:
        print("Validation failed. See errors above.")
        sys.exit(1)


def cmd_render(args):
    import subprocess
    from .registry import list_skills
    tools_dir = Path(__file__).parent.parent.parent / "tools"
    scripts = ["render_openai_skill.py", "render_claude_skill.py", "render_gemini_gem.py"]

    if len(args) > 1:
        render_targets = [args[1:]]
    else:
        render_targets = [[str(skill.path)] for skill in list_skills(SKILLS_DIR)]

    for target_args in render_targets:
        for script in scripts:
            script_path = tools_dir / script
            if script_path.exists():
                result = subprocess.run([sys.executable, str(script_path)] + target_args)
                if result.returncode != 0:
                    print(f"Error running {script}")
                    sys.exit(1)
    print("Render complete.")


def cmd_show(args):
    if len(args) < 2:
        print("Usage: agent-skillbook show <slug>")
        sys.exit(1)
    slug = args[1]
    from .registry import load_skill
    skill_dir = SKILLS_DIR / slug
    skill = load_skill(skill_dir)
    if skill is None:
        print(f"Skill '{slug}' not found.")
        sys.exit(1)
    print(f"Slug:    {skill.slug}")
    print(f"Title:   {skill.title}")
    print(f"Summary: {skill.summary}")
    print(f"Tags:    {', '.join(skill.tags)}")
    print(f"\nWhen to use:")
    for item in skill.when_to_use:
        print(f"  - {item}")
    print(f"\nWhen NOT to use:")
    for item in skill.when_not_to_use:
        print(f"  - {item}")


def main():
    args = sys.argv[1:]
    if not args:
        print("Usage: agent-skillbook <command> [args]")
        print("Commands: list, validate, render, show")
        sys.exit(0)
    command = args[0]
    dispatch = {
        "list": cmd_list,
        "validate": cmd_validate,
        "render": cmd_render,
        "show": cmd_show,
    }
    if command not in dispatch:
        print(f"Unknown command: {command}")
        print("Commands: list, validate, render, show")
        sys.exit(1)
    dispatch[command](args)


if __name__ == "__main__":
    main()
