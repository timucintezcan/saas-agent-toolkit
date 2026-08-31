from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.validate_repository import (
    parse_frontmatter,
    validate_provider_contracts,
    validate_repository,
    validate_skill_catalog,
)


class RepositoryValidatorTest(unittest.TestCase):
    def test_current_repository_is_valid(self) -> None:
        root = Path(__file__).resolve().parents[1]
        self.assertEqual(validate_repository(root), [])

    def test_rejects_mismatched_skill_name(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / ".codex-plugin").mkdir()
            (root / ".codex-plugin" / "plugin.json").write_text(
                json.dumps(
                    {
                        "name": "saas-agent-toolkit",
                        "version": "0.1.0",
                        "skills": "./skills/",
                    }
                ),
                encoding="utf-8",
            )
            skill = root / "skills" / "expected-name"
            (skill / "agents").mkdir(parents=True)
            (skill / "SKILL.md").write_text(
                "---\nname: wrong-name\ndescription: A useful test skill.\n---\n# Test\n",
                encoding="utf-8",
            )
            (skill / "agents" / "openai.yaml").write_text(
                'interface:\n  display_name: "Test"\n  short_description: "Test skill."\n',
                encoding="utf-8",
            )

            self.assertIn(
                "expected-name: frontmatter name must match directory",
                validate_repository(root),
            )

    def test_rejects_unterminated_frontmatter(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            skill_file = Path(directory) / "SKILL.md"
            skill_file.write_text("---\nname: broken\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "unterminated YAML frontmatter"):
                parse_frontmatter(skill_file)

    def test_rejects_marketplace_with_external_plugin_path(self) -> None:
        root = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as directory:
            copy_root = Path(directory)
            marketplace_path = copy_root / ".agents" / "plugins" / "marketplace.json"
            marketplace_path.parent.mkdir(parents=True)
            marketplace_path.write_text(
                json.dumps(
                    {
                        "name": "saas-agent-toolkit",
                        "plugins": [
                            {
                                "name": "saas-agent-toolkit",
                                "source": {
                                    "source": "local",
                                    "path": "../outside",
                                },
                                "policy": {
                                    "installation": "AVAILABLE",
                                    "authentication": "ON_INSTALL",
                                },
                                "category": "Developer Tools",
                            }
                        ],
                    }
                ),
                encoding="utf-8",
            )
            (copy_root / ".codex-plugin").mkdir()
            (copy_root / ".codex-plugin" / "plugin.json").write_text(
                (root / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"),
                encoding="utf-8",
            )
            (copy_root / "skills").mkdir()

            self.assertIn(
                "Marketplace plugin source must point to the repository root",
                validate_repository(copy_root),
            )

    def test_rejects_skill_catalog_drift(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "skills" / "documented-skill").mkdir(parents=True)
            (root / "skills" / "missing-skill").mkdir(parents=True)
            catalog_path = root / "docs" / "skill-catalog.md"
            catalog_path.parent.mkdir()
            catalog_path.write_text(
                "| Skill | Use when |\n"
                "| --- | --- |\n"
                "| `documented-skill` | Documented. |\n"
                "| `unknown-skill` | Unknown. |\n",
                encoding="utf-8",
            )
            errors: list[str] = []

            validate_skill_catalog(root, errors)

            self.assertIn("Skill catalog is missing: missing-skill", errors)
            self.assertIn("Skill catalog contains unknown skills: unknown-skill", errors)

    def test_rejects_provider_without_shared_workflow(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            skill_path = root / "skills" / "example-provider" / "SKILL.md"
            skill_path.parent.mkdir(parents=True)
            skill_path.write_text("# Example Provider\n", encoding="utf-8")
            catalog_path = root / "docs" / "provider-skills.md"
            catalog_path.parent.mkdir()
            catalog_path.write_text(
                "| Skill | Coverage |\n"
                "| --- | --- |\n"
                "| `example-provider` | Example. |\n",
                encoding="utf-8",
            )
            errors: list[str] = []

            validate_provider_contracts(root, errors)

            self.assertIn(
                "example-provider: provider skill must reference provider-integration.md",
                errors,
            )


if __name__ == "__main__":
    unittest.main()
