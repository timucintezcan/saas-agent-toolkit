# SaaS Agent Toolkit Engineering Contract

## Purpose

This repository owns reusable, product-agnostic agent roles, skills, workflows, policies, and deterministic helpers for SaaS engineering.

## Language

All repository content, code, documentation, prompts, examples, commit messages, and user-facing plugin metadata must be written in English.

## Boundaries

- `core/` is the vendor-neutral source of truth.
- `skills/` contains bounded Codex skill adapters and task-specific guidance.
- Provider-specific behavior belongs in provider-specific skills.
- Product business logic and product-specific names do not belong in this repository.
- SaaS Foundation is supported but must never be required.

## Skill Rules

- Discover the target repository before assuming its framework, package manager, cloud, or folder structure.
- Keep activation descriptions narrow and discriminating.
- Define inputs, output, verification, failure behavior, and stopping conditions.
- Do not duplicate shared policies inside every skill; reference the relevant core policy.
- Add scripts only when deterministic automation materially improves safety or reliability.
- Do not include secret values, credentials, private URLs, or copied provider documentation.

## Production Safety

- Read-only inspection may proceed without mutation approval.
- Require explicit human approval immediately before production mutations.
- Never bypass provider permission systems.
- Never disable security controls to make an integration pass.
- Prefer preview, dry-run, and local verification before production work.

## Validation

- Validate every changed skill with the skill validator.
- Validate the plugin manifest after plugin changes.
- Run meaningful script tests when scripts are added or changed.
- Keep changes small, documented, and independently reviewable.
