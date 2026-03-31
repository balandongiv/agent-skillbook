"""Tests for skill registry loading."""
import pytest
from pathlib import Path
from agent_skillbook.registry import load_skill, load_all_skills, list_skills

SKILLS_DIR = Path(__file__).parent.parent / "skills"


def test_load_all_skills_returns_dict():
    skills = load_all_skills(SKILLS_DIR)
    assert isinstance(skills, dict)
    assert len(skills) >= 3


def test_list_skills_returns_list():
    skills = list_skills(SKILLS_DIR)
    assert isinstance(skills, list)
    assert len(skills) >= 3


def test_skill_has_required_attributes():
    skills = list_skills(SKILLS_DIR)
    for skill in skills:
        assert skill.slug
        assert skill.title
        assert skill.summary
        assert isinstance(skill.tags, list)


def test_load_specific_skill():
    skill_dir = SKILLS_DIR / "good-function-design"
    skill = load_skill(skill_dir)
    assert skill is not None
    assert skill.slug == "good-function-design"
    assert skill.title


def test_load_nonexistent_skill_returns_none():
    skill_dir = SKILLS_DIR / "nonexistent-skill"
    skill = load_skill(skill_dir)
    assert skill is None
