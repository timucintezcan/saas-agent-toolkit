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


if __name__ == "__main__":
    unittest.main()
