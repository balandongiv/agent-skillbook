"""Validators for canonical skill files and repository version metadata."""
import re
from pathlib import Path
from typing import List, Tuple

REQUIRED_FILES = ["skill.yaml", "INSTRUCTIONS.md", "EXAMPLES.md", "TESTS.md", "CHANGELOG.md"]
REQUIRED_YAML_FIELDS = ["slug", "title", "summary", "when_to_use", "when_not_to_use", "tags", "invocation"]
KEBAB_CASE_RE = re.compile(r"^[a-z][a-z0-9-]*$")
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")
CHANGELOG_RELEASE_RE = re.compile(r"^## \[(\d+\.\d+\.\d+)\] - \d{4}-\d{2}-\d{2}$", re.MULTILINE)
PYPROJECT_VERSION_RE = re.compile(r'^version\s*=\s*"([^"]+)"\s*$', re.MULTILINE)
INIT_VERSION_RE = re.compile(r'^__version__\s*=\s*"([^"]+)"\s*$', re.MULTILINE)
README_VERSION_RE = re.compile(r'^Status:\s.*\|\sVersion:\s([^\s|]+)\s\|', re.MULTILINE)

ValidationResult = Tuple[bool, List[str]]


def _extract_with_regex(path: Path, pattern: re.Pattern[str], label: str) -> Tuple[str, List[str]]:
    if not path.exists():
        return "", [f"Missing required file: {path.name}"]

    text = path.read_text(encoding="utf-8")
    match = pattern.search(text)
    if not match:
        return "", [f"Could not find {label} in {path.name}"]

    return match.group(1), []


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


def validate_skill_changelog(skill_dir: Path) -> ValidationResult:
    errors = []
    changelog_path = skill_dir / "CHANGELOG.md"
    if not changelog_path.exists():
        return False, ["CHANGELOG.md not found"]

    text = changelog_path.read_text(encoding="utf-8")

    if "## [Unreleased]" not in text:
        errors.append("CHANGELOG.md must contain an '## [Unreleased]' section for pending changes")

    releases = CHANGELOG_RELEASE_RE.findall(text)
    if not releases:
        errors.append("CHANGELOG.md must contain at least one released version heading like '## [0.1.0] - YYYY-MM-DD'")
    else:
        invalid_versions = [version for version in releases if not SEMVER_RE.match(version)]
        if invalid_versions:
            errors.append(f"CHANGELOG.md contains invalid semantic versions: {', '.join(invalid_versions)}")

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
    for validator in [
        validate_skill_dir_name,
        validate_required_files,
        validate_yaml_fields,
        validate_skill_changelog,
        validate_exports,
    ]:
        ok, errors = validator(skill_dir)
        all_errors.extend(errors)
    return len(all_errors) == 0, all_errors


def validate_repository_versioning(repo_root: Path) -> ValidationResult:
    errors = []

    pyproject_version, pyproject_errors = _extract_with_regex(
        repo_root / "pyproject.toml",
        PYPROJECT_VERSION_RE,
        "project.version",
    )
    errors.extend(pyproject_errors)

    init_version, init_errors = _extract_with_regex(
        repo_root / "src" / "agent_skillbook" / "__init__.py",
        INIT_VERSION_RE,
        "__version__",
    )
    errors.extend(init_errors)

    readme_version, readme_errors = _extract_with_regex(
        repo_root / "README.md",
        README_VERSION_RE,
        "README status version",
    )
    errors.extend(readme_errors)

    root_changelog = repo_root / "CHANGELOG.md"
    if not root_changelog.exists():
        errors.append("Missing required file: CHANGELOG.md")
    else:
        changelog_text = root_changelog.read_text(encoding="utf-8")
        if "## [Unreleased]" not in changelog_text:
            errors.append("Root CHANGELOG.md must contain an '## [Unreleased]' section")

    if pyproject_version and not SEMVER_RE.match(pyproject_version):
        errors.append(f"pyproject.toml version '{pyproject_version}' must use semantic versioning (X.Y.Z)")

    if pyproject_version and init_version and pyproject_version != init_version:
        errors.append(
            f"Version mismatch: pyproject.toml has {pyproject_version} but src/agent_skillbook/__init__.py has {init_version}"
        )

    if pyproject_version and readme_version and pyproject_version != readme_version:
        errors.append(
            f"Version mismatch: pyproject.toml has {pyproject_version} but README.md shows {readme_version}"
        )

    return len(errors) == 0, errors


def validate_all_skills(skills_dir: Path) -> dict:
    results = {}
    if not skills_dir.exists():
        return results
    for skill_dir in sorted(skills_dir.iterdir()):
        if skill_dir.is_dir() and not skill_dir.name.startswith("."):
            ok, errors = validate_skill(skill_dir)
            results[skill_dir.name] = {"ok": ok, "errors": errors}
    return results
