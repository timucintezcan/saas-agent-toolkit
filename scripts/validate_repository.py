#!/usr/bin/env python3

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


FRONTMATTER_BOUNDARY = "---"
LOCAL_LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def parse_frontmatter(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != FRONTMATTER_BOUNDARY:
        raise ValueError(f"{path}: missing YAML frontmatter")

    try:
        end = lines.index(FRONTMATTER_BOUNDARY, 1)
    except ValueError as error:
        raise ValueError(f"{path}: unterminated YAML frontmatter") from error

    values: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"{path}: unsupported frontmatter line: {line}")
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def validate_plugin(root: Path, errors: list[str]) -> None:
    manifest_path = root / ".codex-plugin" / "plugin.json"
    if not manifest_path.is_file():
        errors.append("Missing .codex-plugin/plugin.json")
        return

    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        errors.append(f"Invalid plugin JSON: {error}")
        return

    if manifest.get("name") != "saas-agent-toolkit":
        errors.append("Plugin name must be saas-agent-toolkit")
    if not manifest.get("version"):
        errors.append("Plugin version is required")
    if manifest.get("skills") != "./skills/":
        errors.append("Plugin skills path must be ./skills/")


def validate_marketplace(root: Path, errors: list[str]) -> None:
    marketplace_path = root / ".agents" / "plugins" / "marketplace.json"
    if not marketplace_path.is_file():
        errors.append("Missing .agents/plugins/marketplace.json")
        return

    try:
        marketplace = json.loads(marketplace_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        errors.append(f"Invalid marketplace JSON: {error}")
        return

    if marketplace.get("name") != "saas-agent-toolkit":
        errors.append("Marketplace name must be saas-agent-toolkit")

    plugins = marketplace.get("plugins")
    if not isinstance(plugins, list):
        errors.append("Marketplace plugins must be an array")
        return

    plugin = next(
        (entry for entry in plugins if entry.get("name") == "saas-agent-toolkit"),
        None,
    )
    if plugin is None:
        errors.append("Marketplace must expose saas-agent-toolkit")
        return

    if plugin.get("source") != {"source": "local", "path": "."}:
        errors.append("Marketplace plugin source must point to the repository root")
    if plugin.get("policy") != {
        "installation": "AVAILABLE",
        "authentication": "ON_INSTALL",
    }:
        errors.append("Marketplace plugin policy must use the safe public defaults")
    if plugin.get("category") != "Developer Tools":
        errors.append("Marketplace plugin category must be Developer Tools")


def validate_skills(root: Path, errors: list[str]) -> None:
    skills_root = root / "skills"
    if not skills_root.is_dir():
        errors.append("Missing skills directory")
        return

    skill_directories = sorted(path for path in skills_root.iterdir() if path.is_dir())
    if not skill_directories:
        errors.append("No skills found")
        return

    for skill_directory in skill_directories:
        skill_file = skill_directory / "SKILL.md"
        metadata_file = skill_directory / "agents" / "openai.yaml"

        if not skill_file.is_file():
            errors.append(f"{skill_directory.name}: missing SKILL.md")
            continue

        try:
            frontmatter = parse_frontmatter(skill_file)
        except ValueError as error:
            errors.append(str(error))
            continue

        if frontmatter.get("name") != skill_directory.name:
            errors.append(f"{skill_directory.name}: frontmatter name must match directory")

        description = frontmatter.get("description", "")
        if not description or "TODO" in description:
            errors.append(f"{skill_directory.name}: meaningful description is required")

        content = skill_file.read_text(encoding="utf-8")
        if "[TODO" in content or "TODO:" in content:
            errors.append(f"{skill_directory.name}: unfinished scaffold marker found")

        if not metadata_file.is_file():
            errors.append(f"{skill_directory.name}: missing agents/openai.yaml")
            continue

        metadata = metadata_file.read_text(encoding="utf-8")
        for required_key in ("interface:", "display_name:", "short_description:"):
            if required_key not in metadata:
                errors.append(f"{skill_directory.name}: openai.yaml missing {required_key}")


def validate_markdown_links(root: Path, errors: list[str]) -> None:
    ignored_parts = {".git", "node_modules"}
    for markdown_file in sorted(root.rglob("*.md")):
        if ignored_parts.intersection(markdown_file.parts):
            continue
        content = markdown_file.read_text(encoding="utf-8")
        for target in LOCAL_LINK_PATTERN.findall(content):
            target = target.strip().split("#", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            resolved = (markdown_file.parent / target).resolve()
            if not resolved.exists():
                relative_file = markdown_file.relative_to(root)
                errors.append(f"{relative_file}: broken local link {target}")


def validate_repository(root: Path) -> list[str]:
    errors: list[str] = []
    validate_plugin(root, errors)
    validate_marketplace(root, errors)
    validate_skills(root, errors)
    validate_markdown_links(root, errors)
    return errors


def main() -> int:
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    errors = validate_repository(root)

    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    skill_count = sum(1 for path in (root / "skills").iterdir() if path.is_dir())
    print(f"Repository validation passed with {skill_count} skills.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
