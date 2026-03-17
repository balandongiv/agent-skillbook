"""Tests for skill renderers."""
import subprocess
import sys
import pytest
from pathlib import Path

TOOLS_DIR = Path(__file__).parent.parent / "tools"
SKILLS_DIR = Path(__file__).parent.parent / "skills"


def run_renderer(script_name, skill_slug, tmp_path):
    """Run a renderer script for a skill and capture output."""
    script = TOOLS_DIR / script_name
    skill_dir = SKILLS_DIR / skill_slug
    result = subprocess.run(
        [sys.executable, str(script), str(skill_dir), str(tmp_path)],
        capture_output=True,
        text=True,
    )
    return result


def test_render_openai_skill(tmp_path):
    result = run_renderer("render_openai_skill.py", "good-function-design", tmp_path)
    assert result.returncode == 0, f"stdout: {result.stdout}\nstderr: {result.stderr}"
    output_file = tmp_path / "SKILL.md"
    assert output_file.exists()
    content = output_file.read_text()
    assert "name:" in content or "---" in content


def test_render_claude_skill(tmp_path):
    result = run_renderer("render_claude_skill.py", "good-function-design", tmp_path)
    assert result.returncode == 0, f"stdout: {result.stdout}\nstderr: {result.stderr}"
    output_file = tmp_path / "SKILL.md"
    assert output_file.exists()
    content = output_file.read_text()
    assert "---" in content


def test_render_gemini_gem(tmp_path):
    result = run_renderer("render_gemini_gem.py", "good-function-design", tmp_path)
    assert result.returncode == 0, f"stdout: {result.stdout}\nstderr: {result.stderr}"
    output_file = tmp_path / "GEM_INSTRUCTIONS.md"
    assert output_file.exists()
