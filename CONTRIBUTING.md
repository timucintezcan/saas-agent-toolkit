# Contributing

Thank you for improving SaaS Agent Toolkit. Contributions should make repeated SaaS engineering work safer, clearer, or more reliable without coupling the toolkit to one product.

## Contribution Types

- Vendor-neutral roles, policies, and workflows
- Specialist agent outcome contracts
- Focused Codex role or procedure skills
- Provider integration skills
- Deterministic validators and setup helpers
- Behavioral tests and representative fixtures
- Documentation and installation improvements

## Choose the Correct Layer

| Change | Location |
| --- | --- |
| Durable engineering responsibility | `core/roles/` |
| Cross-cutting safety or portability invariant | `core/policies/` |
| Shared execution sequence or task contract | `core/workflows/` |
| Specialist ownership and output contract | `agents/` |
| Codex activation and bounded procedure | `skills/` |
| Provider-specific mechanics | A focused provider skill under `skills/` |
| Deterministic structural check | `scripts/` with tests in `tests/` |

Do not duplicate shared rules across several skills. Reference the core source of truth instead.

## Skill Quality Bar

A skill must:

1. Solve a bounded, repeated SaaS engineering task.
2. State a narrow activation description in valid frontmatter.
3. Discover repository context instead of assuming a fixed layout.
4. Preserve user intent and existing architecture.
5. Define inputs, outputs, verification, failure behavior, and stopping conditions.
6. Separate repository preparation from external or production mutation.
7. Apply approval and secret-handling policies where relevant.
8. Avoid private data, copied provider manuals, and product-specific assumptions.
9. Include `agents/openai.yaml` metadata.
10. Pass canonical skill validation and repository validation.

## Agent Profile Quality Bar

An agent profile must define:

- mission and activation boundary;
- responsibilities and non-responsibilities;
- delegation and escalation boundaries;
- approval-sensitive decisions;
- a concrete output contract;
- relationships to existing specialist profiles.

Create a new profile only when the outcome ownership is durable and cannot be represented as a narrower skill under an existing specialist.

## Provider Skill Rules

- Store durable decisions and invariants, not copied dashboard instructions.
- Consult current official documentation or installed CLI help when exact behavior may have changed.
- Never request secret values in chat or print them in logs.
- Prefer preview, dry-run, and local validation.
- Require explicit approval immediately before external production mutation.
- Define verification and rollback evidence; do not report success from configuration alone.

## Development Workflow

1. Open an issue or concise design note for a broad capability.
2. Identify the correct ownership layer before editing.
3. Keep the change product-agnostic and independently reviewable.
4. Add or update deterministic tests when validation behavior changes.
5. Validate all changed skills and the plugin manifest.
6. Test observable behavior against a representative repository.
7. Update the skill catalog, usage guidance, and changelog when public behavior changes.

## Validation

Run the portable checks:

```bash
python3 scripts/validate_repository.py
python3 -m unittest discover -s tests -p "test_*.py"
```

Also run the canonical Codex skill validator for changed skills and the canonical Codex plugin validator before release. Their filesystem locations are environment-specific and should not be hard-coded into repository scripts.

## Pull Request Checklist

- [ ] The change belongs in this repository and the selected layer.
- [ ] Repository discovery remains the first execution step where applicable.
- [ ] Activation language is narrow and does not overlap unnecessarily.
- [ ] Production and external mutation gates are explicit.
- [ ] Secret values cannot enter prompts, logs, fixtures, or committed files.
- [ ] Verification and failure behavior are observable.
- [ ] Tests and documentation reflect public behavior.
- [ ] Repository, skill, and plugin validation pass.

## Commit Style

Use concise English commit messages. Conventional prefixes such as `feat:`, `fix:`, `docs:`, `test:`, and `ci:` are recommended.
