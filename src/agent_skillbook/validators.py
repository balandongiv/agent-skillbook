"""Validators for canonical skill files."""
import re
from pathlib import Path
from typing import List, Tuple

REQUIRED_FILES = ["skill.yaml", "INSTRUCTIONS.md", "EXAMPLES.md", "TESTS.md", "CHANGELOG.md"]
REQUIRED_YAML_FIELDS = ["slug", "title", "summary", "when_to_use", "when_not_to_use", "tags", "invocation"]
KEBAB_CASE_RE = re.compile(r"^[a-z][a-z0-9-]*$")

ValidationResult = Tuple[bool, List[str]]


def validate_skill_dir_name(skill_dir: Path) -> ValidationResult:
    errors = []
    if not KEBAB_CASE_RE.match(skill_dir.name):
        errors.append(f"Folder name '{skill_dir.name}' must be lowercase kebab-case")
    return len(errors) == 0, errors


def validate_required_files(skill_dir: Path) -> ValidationResult:
    errors = []
    for fname in REQUIRED_FILES:
        if not (skill_dir / fname).exists():
            errors.append(f"Missing required file: {fname}")
    return len(errors) == 0, errors


def validate_yaml_fields(skill_dir: Path) -> ValidationResult:
    import yaml
    errors = []
    yaml_path = skill_dir / "skill.yaml"
    if not yaml_path.exists():
        return False, ["skill.yaml not found"]
    with open(yaml_path) as f:
        data = yaml.safe_load(f) or {}
    for field in REQUIRED_YAML_FIELDS:
        if field not in data or data[field] is None:
            errors.append(f"Missing required YAML field: {field}")
    return len(errors) == 0, errors


def validate_exports(skill_dir: Path) -> ValidationResult:
    errors = []
    exports_dir = skill_dir / "exports"
    checks = [
        exports_dir / "openai" / "SKILL.md",
        exports_dir / "claude" / "SKILL.md",
        exports_dir / "gemini" / "GEM_INSTRUCTIONS.md",
    ]
    for path in checks:
        if not path.exists():
            errors.append(f"Missing export: {path.relative_to(skill_dir)}")
        elif path.stat().st_size == 0:
            errors.append(f"Export is empty: {path.relative_to(skill_dir)}")
    return len(errors) == 0, errors


def validate_skill(skill_dir: Path) -> ValidationResult:
    all_errors = []
    for validator in [validate_skill_dir_name, validate_required_files, validate_yaml_fields, validate_exports]:
        ok, errors = validator(skill_dir)
        all_errors.extend(errors)
    return len(all_errors) == 0, all_errors


def validate_all_skills(skills_dir: Path) -> dict:
    results = {}
    if not skills_dir.exists():
        return results
    for skill_dir in sorted(skills_dir.iterdir()):
        if skill_dir.is_dir() and not skill_dir.name.startswith("."):
            ok, errors = validate_skill(skill_dir)
            results[skill_dir.name] = {"ok": ok, "errors": errors}
    return results
