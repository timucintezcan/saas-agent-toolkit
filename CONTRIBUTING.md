# Contributing

Thank you for improving SaaS Agent Toolkit.

## Contribution Types

- Vendor-neutral agent roles and workflows
- Focused provider integration skills
- Deterministic validation or setup scripts
- Behavioral tests and fixtures
- Documentation corrections

## Skill Quality Bar

A skill must:

1. Solve a bounded, repeated SaaS engineering task.
2. State when it should and should not activate.
3. Discover repository context instead of assuming a fixed layout.
4. Preserve user intent and existing architecture.
5. Define required approvals for external or production mutations.
6. Include verification and failure behavior.
7. Avoid secrets, private data, and product-specific assumptions.

## Development Process

1. Open an issue or short design note for a new broad capability.
2. Keep shared rules in `core/` and adapter behavior in `skills/`.
3. Validate changed skills and the plugin manifest.
4. Test observable behavior with a representative repository fixture.
5. Submit a focused pull request explaining scope, risks, and verification.

## Commit Style

Use concise English commit messages. Conventional prefixes such as `feat:`, `fix:`, `docs:`, and `test:` are recommended.
