"""Data models for agent skills."""
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional
from pathlib import Path


@dataclass
class Invocation:
    auto: bool = True
    explicit: bool = True


@dataclass
class Skill:
    slug: str
    title: str
    summary: str
    when_to_use: List[str] = field(default_factory=list)
    when_not_to_use: List[str] = field(default_factory=list)
    tags: List[str] = field(default_factory=list)
    invocation: Optional[Invocation] = None
    platform_overrides: Dict[str, Any] = field(default_factory=dict)
    path: Optional[Path] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any], path: Optional[Path] = None) -> "Skill":
        invocation_data = data.get("invocation", {})
        invocation = Invocation(
            auto=invocation_data.get("auto", True),
            explicit=invocation_data.get("explicit", True),
        ) if invocation_data else None
        return cls(
            slug=data.get("slug", ""),
            title=data.get("title", ""),
            summary=data.get("summary", ""),
            when_to_use=data.get("when_to_use", []),
            when_not_to_use=data.get("when_not_to_use", []),
            tags=data.get("tags", []),
            invocation=invocation,
            platform_overrides=data.get("platform_overrides", {}),
            path=path,
        )
