"""Helpers for canonical repository version metadata."""

from __future__ import annotations

import re
from pathlib import Path


VERSION_FILE_NAME = "VERSION"
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")
PYPROJECT_VERSION_RE = re.compile(r'^version\s*=\s*"([^"]+)"\s*$', re.MULTILINE)
INIT_VERSION_RE = re.compile(r'^__version__\s*=\s*"([^"]+)"\s*$', re.MULTILINE)
README_VERSION_RE = re.compile(r'^Status:\s.*\|\sVersion:\s([^\s|]+)(\s\|.*)$', re.MULTILINE)


def read_canonical_version(repo_root: Path) -> str:
    """Return the canonical repository version from VERSION."""

    version_path = repo_root / VERSION_FILE_NAME
    if not version_path.exists():
        raise FileNotFoundError(f"Missing required file: {VERSION_FILE_NAME}")

    version = version_path.read_text(encoding="utf-8").strip()
    if not SEMVER_RE.match(version):
        raise ValueError(
            f"{VERSION_FILE_NAME} value '{version}' must use semantic versioning (X.Y.Z)"
        )
    return version


def write_canonical_version(repo_root: Path, version: str) -> None:
    """Write the canonical repository version to VERSION."""

    if not SEMVER_RE.match(version):
        raise ValueError(f"Version '{version}' must use semantic versioning (X.Y.Z)")
    (repo_root / VERSION_FILE_NAME).write_text(f"{version}\n", encoding="utf-8")


def bump_semver(version: str, part: str) -> str:
    """Return the next semantic version for the requested part."""

    if not SEMVER_RE.match(version):
        raise ValueError(f"Version '{version}' must use semantic versioning (X.Y.Z)")

    major, minor, patch = (int(value) for value in version.split("."))
    normalised_part = part.lower()
    if normalised_part == "major":
        return f"{major + 1}.0.0"
    if normalised_part == "minor":
        return f"{major}.{minor + 1}.0"
    if normalised_part == "patch":
        return f"{major}.{minor}.{patch + 1}"
    raise ValueError(f"Unsupported version bump part: {part}")


def _replace_version_with_regex(
    path: Path,
    pattern: re.Pattern[str],
    replacement,
    *,
    label: str,
) -> None:
    """Replace the first version occurrence in one file."""

    text = path.read_text(encoding="utf-8")
    updated_text, replacement_count = pattern.subn(replacement, text, count=1)
    if replacement_count != 1:
        raise ValueError(f"Could not update {label} in {path.name}")
    path.write_text(updated_text, encoding="utf-8")


def sync_repository_versioning(repo_root: Path, *, version: str | None = None) -> str:
    """Synchronize version metadata files from the canonical VERSION value."""

    resolved_version = version or read_canonical_version(repo_root)
    write_canonical_version(repo_root, resolved_version)

    _replace_version_with_regex(
        repo_root / "pyproject.toml",
        PYPROJECT_VERSION_RE,
        lambda match: match.group(0).replace(match.group(1), resolved_version),
        label="project.version",
    )
    _replace_version_with_regex(
        repo_root / "src" / "agent_skillbook" / "__init__.py",
        INIT_VERSION_RE,
        lambda match: match.group(0).replace(match.group(1), resolved_version),
        label="__version__",
    )
    _replace_version_with_regex(
        repo_root / "README.md",
        README_VERSION_RE,
        lambda match: f"{match.group(0).replace(match.group(1), resolved_version)}",
        label="README status version",
    )
    return resolved_version


def bump_repository_version(repo_root: Path, *, part: str = "patch") -> str:
    """Bump the canonical version and synchronize repository metadata."""

    current_version = read_canonical_version(repo_root)
    next_version = bump_semver(current_version, part=part)
    return sync_repository_versioning(repo_root, version=next_version)
