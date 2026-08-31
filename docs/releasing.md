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
- known limitations and deferred adapter capabilities.

## Current `0.1.0` Evidence

- The repository validator passes with seventeen skills.
- Python unit tests pass.
- The Codex plugin validator passes.
- The repository can be registered directly as a Codex marketplace without duplicating plugin files.
- The local plugin installs as enabled with eight agent profiles and seventeen skills.
- Read-only evaluation against KitapBuurt confirmed environment, Supabase, Vercel, OpenAI, and release-readiness behavior without changing the target repository.

## Current `0.1.1` Evidence

- The public documentation is reorganized around onboarding, skill discovery, usage patterns, architecture, contribution, and security.
- The skill catalog contains one entry for each of the seventeen installed skill directories.
- Repository, unit, and canonical plugin validation pass.
- The release preserves the `0.1.x` agent, skill, approval, and provider contracts.

## Current `0.2.0` Evidence

- The repository validator passes with twenty-one skills and eight Claude-compatible agent profiles.
- Python unit tests pass.
- Codex plugin manifest and marketplace contracts validate through the repository validator.
- Claude Code CLI validates the plugin without warnings.
- Foundation generator contracts, provider skills, shared UI-assisted execution, and native Claude Code support remain optional for generated applications.
- Known limitation: the adapter ships shared skills and specialist subagents only; provider-specific MCP servers, hooks, and Claude-only automation are deliberately not bundled.

## Current `0.3.0` Evidence

- The repository validator passes with twenty-two skills and eight Claude-compatible agent profiles.
- Python unit tests pass.
- The Codex and Claude plugin manifests carry matching `0.3.0` versions.
- The hybrid mobile-delivery workflow keeps one mobile-first web UI as the product surface and isolates device capabilities behind Capacitor adapters.
- The SaaS Bootstrap Advisor distinguishes the managed-backend web, hybrid, custom API, worker, and separate native application paths.
- Known limitation: native platform project creation, code signing, store accounts, permissions, and store submission remain explicit human-owned steps.
