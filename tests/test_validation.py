"""Tests for skill validation."""
import pytest
from pathlib import Path
from agent_skillbook.validators import (
    validate_skill,
    validate_all_skills,
    validate_skill_dir_name,
    validate_required_files,
    validate_yaml_fields,
    validate_exports,
)

SKILLS_DIR = Path(__file__).parent.parent / "skills"


def test_all_starter_skills_are_valid():
    results = validate_all_skills(SKILLS_DIR)
    assert len(results) >= 3
    for name, result in results.items():
        assert result["ok"], f"Skill '{name}' failed validation: {result['errors']}"


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


def test_good_function_design_exports():
    skill_dir = SKILLS_DIR / "good-function-design"
    ok, errors = validate_exports(skill_dir)
    assert ok, f"Export errors: {errors}"
