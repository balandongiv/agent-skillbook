"""Registry for loading canonical skills from the skills/ directory."""
from pathlib import Path
from typing import Dict, List, Optional
import yaml
from .models import Skill

DEFAULT_SKILLS_DIR = Path(__file__).parent.parent.parent / "skills"


def load_skill(skill_dir: Path) -> Optional[Skill]:
    yaml_path = skill_dir / "skill.yaml"
    if not yaml_path.exists():
        return None
    with open(yaml_path) as f:
        data = yaml.safe_load(f)
    return Skill.from_dict(data, path=skill_dir)


def load_all_skills(skills_dir: Path = DEFAULT_SKILLS_DIR) -> Dict[str, Skill]:
    skills = {}
    if not skills_dir.exists():
        return skills
    for skill_dir in sorted(skills_dir.iterdir()):
        if skill_dir.is_dir() and not skill_dir.name.startswith("."):
            skill = load_skill(skill_dir)
            if skill:
                skills[skill.slug] = skill
    return skills


def list_skills(skills_dir: Path = DEFAULT_SKILLS_DIR) -> List[Skill]:
    return list(load_all_skills(skills_dir).values())
