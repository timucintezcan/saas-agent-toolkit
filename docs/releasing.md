# Release Process

## Release Checklist

1. Confirm the working tree is clean and the target branch is current.
2. Run the repository validator and unit tests.
3. Run the canonical Codex skill validator for every skill.
4. Run the canonical Codex plugin validator.
5. Install the plugin through a local marketplace and verify that Codex reports it as enabled.
6. Confirm the installed cache contains all expected agent profiles, skills, and shared contracts.
7. Test the Git marketplace installation command against the release commit or tag.
8. Validate at least one role skill and one provider skill against a real repository without unintended mutation.
9. Review `CHANGELOG.md`, documentation, security boundaries, and approval gates.
10. Create an annotated semantic version tag.
11. Publish a GitHub Release with installation, compatibility, validation, and known-limit notes.

## Validation Commands

```bash
python3 scripts/validate_repository.py
python3 -m unittest discover -s tests -p "test_*.py"
```

Run the canonical validators from the installed Codex skill and plugin tooling before tagging. Their filesystem locations are environment-specific and should not be embedded in repository scripts.

## Release Evidence

Record the following in the release notes:

- commit SHA and version;
- CI run result;
- repository validation result;
- plugin installation and discovery result;
- real-project evaluation scope;
- supported Codex version or environment;
- known limitations and deferred adapters.

## Current `0.1.0` Evidence

- The repository validator passes with seventeen skills.
- Python unit tests pass.
- The Codex plugin validator passes.
- The repository can be registered directly as a Codex marketplace without duplicating plugin files.
- The local plugin installs as enabled with eight agent profiles and seventeen skills.
- Read-only evaluation against KitapBuurt confirmed environment, Supabase, Vercel, OpenAI, and release-readiness behavior without changing the target repository.
- Claude Code support is intentionally deferred until the Codex workflows stabilize.
