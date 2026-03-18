"""Tests for skill validation."""
import pytest
from pathlib import Path
from agent_skillbook.validators import (
    validate_skill,
    validate_all_skills,
    validate_repository_versioning,
    validate_skill_dir_name,
    validate_required_files,
    validate_skill_changelog,
    validate_yaml_fields,
    validate_exports,
)
from agent_skillbook.versioning import bump_repository_version, sync_repository_versioning

SKILLS_DIR = Path(__file__).parent.parent / "skills"
REPO_ROOT = Path(__file__).parent.parent


def test_all_starter_skills_are_valid():
    results = validate_all_skills(SKILLS_DIR)
    assert len(results) >= 3
    for name, result in results.items():
        assert result["ok"], f"Skill '{name}' failed validation: {result['errors']}"


def test_repository_versioning_is_consistent():
    ok, errors = validate_repository_versioning(REPO_ROOT)
    assert ok, f"Repository version metadata failed validation: {errors}"


def test_repository_versioning_detects_version_mismatch(tmp_path):
    (tmp_path / "src" / "agent_skillbook").mkdir(parents=True)
    (tmp_path / "VERSION").write_text("1.2.3\n", encoding="utf-8")
    (tmp_path / "pyproject.toml").write_text(
        "[project]\nversion = \"1.2.3\"\n",
        encoding="utf-8",
    )
    (tmp_path / "src" / "agent_skillbook" / "__init__.py").write_text(
        '__version__ = "1.2.2"\n',
        encoding="utf-8",
    )
    (tmp_path / "README.md").write_text(
        "Status: Active | Version: 1.2.3 | License: MIT | Python: >=3.9\n",
        encoding="utf-8",
    )
    (tmp_path / "CHANGELOG.md").write_text(
        "# Changelog\n\n## [Unreleased]\n\n### Changed\n- Pending changes\n",
        encoding="utf-8",
    )

    ok, errors = validate_repository_versioning(tmp_path)
    assert not ok
    assert any("Version mismatch" in error for error in errors)


def test_repository_versioning_requires_version_file(tmp_path):
    (tmp_path / "src" / "agent_skillbook").mkdir(parents=True)
    (tmp_path / "pyproject.toml").write_text(
        "[project]\nversion = \"1.2.3\"\n",
        encoding="utf-8",
    )
    (tmp_path / "src" / "agent_skillbook" / "__init__.py").write_text(
        '__version__ = "1.2.3"\n',
        encoding="utf-8",
    )
    (tmp_path / "README.md").write_text(
        "Status: Active | Version: 1.2.3 | License: MIT | Python: >=3.9\n",
        encoding="utf-8",
    )
    (tmp_path / "CHANGELOG.md").write_text(
        "# Changelog\n\n## [Unreleased]\n\n### Changed\n- Pending changes\n",
        encoding="utf-8",
    )

    ok, errors = validate_repository_versioning(tmp_path)
    assert not ok
    assert any("VERSION" in error for error in errors)


def test_sync_repository_versioning_updates_all_metadata(tmp_path):
    (tmp_path / "src" / "agent_skillbook").mkdir(parents=True)
    (tmp_path / "VERSION").write_text("2.0.0\n", encoding="utf-8")
    (tmp_path / "pyproject.toml").write_text(
        "[project]\nversion = \"1.0.0\"\n",
        encoding="utf-8",
    )
    (tmp_path / "src" / "agent_skillbook" / "__init__.py").write_text(
        '__version__ = "1.0.0"\n',
        encoding="utf-8",
    )
    (tmp_path / "README.md").write_text(
        "# agent-skillbook\n\nStatus: Active | Version: 1.0.0 | License: MIT | Python: >=3.9\n",
        encoding="utf-8",
    )

    resolved_version = sync_repository_versioning(tmp_path)
    assert resolved_version == "2.0.0"
    assert 'version = "2.0.0"' in (tmp_path / "pyproject.toml").read_text(encoding="utf-8")
    assert '__version__ = "2.0.0"' in (tmp_path / "src" / "agent_skillbook" / "__init__.py").read_text(encoding="utf-8")
    assert "Version: 2.0.0" in (tmp_path / "README.md").read_text(encoding="utf-8")


def test_bump_repository_version_updates_version_file(tmp_path):
    (tmp_path / "src" / "agent_skillbook").mkdir(parents=True)
    (tmp_path / "VERSION").write_text("1.2.3\n", encoding="utf-8")
    (tmp_path / "pyproject.toml").write_text(
        "[project]\nversion = \"1.2.3\"\n",
        encoding="utf-8",
    )
    (tmp_path / "src" / "agent_skillbook" / "__init__.py").write_text(
        '__version__ = "1.2.3"\n',
        encoding="utf-8",
    )
    (tmp_path / "README.md").write_text(
        "# agent-skillbook\n\nStatus: Active | Version: 1.2.3 | License: MIT | Python: >=3.9\n",
        encoding="utf-8",
    )

    resolved_version = bump_repository_version(tmp_path, part="patch")
    assert resolved_version == "1.2.4"
    assert (tmp_path / "VERSION").read_text(encoding="utf-8").strip() == "1.2.4"


def test_kebab_case_valid():
    from pathlib import Path
    p = Path("/fake/good-function-design")
    ok, errors = validate_skill_dir_name(p)
    assert ok


def test_kebab_case_invalid():
    p = Path("/fake/BadSkillName")
    ok, errors = validate_skill_dir_name(p)
    assert not ok


def test_good_function_design_has_required_files():
    skill_dir = SKILLS_DIR / "good-function-design"
    ok, errors = validate_required_files(skill_dir)
    assert ok, f"Missing files: {errors}"


def test_good_function_design_yaml_fields():
    skill_dir = SKILLS_DIR / "good-function-design"
    ok, errors = validate_yaml_fields(skill_dir)
    assert ok, f"YAML errors: {errors}"


def test_good_function_design_changelog_has_unreleased_section():
    skill_dir = SKILLS_DIR / "good-function-design"
    ok, errors = validate_skill_changelog(skill_dir)
    assert ok, f"Changelog errors: {errors}"


def test_good_function_design_exports():
    skill_dir = SKILLS_DIR / "good-function-design"
    ok, errors = validate_exports(skill_dir)
    assert ok, f"Export errors: {errors}"


def test_skill_changelog_requires_unreleased_section(tmp_path):
    skill_dir = tmp_path / "example-skill"
    skill_dir.mkdir()
    (skill_dir / "CHANGELOG.md").write_text(
        "# Changelog: Example Skill\n\n## [0.1.0] - 2026-03-17\n\n### Added\n- Initial version\n",
        encoding="utf-8",
    )

    ok, errors = validate_skill_changelog(skill_dir)
    assert not ok
    assert any("[Unreleased]" in error for error in errors)

