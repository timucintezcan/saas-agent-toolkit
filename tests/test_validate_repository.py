from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.validate_repository import parse_frontmatter, validate_repository


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


if __name__ == "__main__":
    unittest.main()
