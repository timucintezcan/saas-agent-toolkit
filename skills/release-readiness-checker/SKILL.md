---
name: release-readiness-checker
description: Produce evidence-based SaaS release readiness reports from repository checks and acceptance criteria. Use before preview, production, tagging, or public template releases.
---

# Release Readiness Checker

## Objective

Return a defensible `GO`, `GO WITH KNOWN RISKS`, or `NO-GO` decision without hiding failed critical checks.

## Workflow

1. Discover repository instructions, release commands, environments, migrations, and acceptance criteria.
2. Classify the release target: local package, preview, production, template, or plugin.
3. Run focused checks first, then the repository's complete release verification.
4. Verify generated artifacts, migration order, environment-variable names, and documentation affected by the change.
5. For hosted releases, use preview or dry-run evidence before requesting production approval.
6. Record commands, results, skipped checks, known risks, rollback path, and required manual tests.

## Decision Rules

- `GO`: all critical checks pass and no unresolved release blocker exists.
- `GO WITH KNOWN RISKS`: critical checks pass; explicitly accepted non-blocking risks remain.
- `NO-GO`: a critical check fails, required evidence is missing, or the target cannot be safely identified.

Do not mutate production while performing readiness assessment. Follow `../../core/workflows/release-lifecycle.md` and `../../core/policies/approval-gates.md`.
