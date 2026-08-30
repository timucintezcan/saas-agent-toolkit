---
name: foundation-scaffold-guardian
description: Protect a reusable SaaS foundation from product-specific drift and unsafe structural changes. Use when changing template layout, workspace boundaries, generator behavior, stack defaults, or shared packages.
---

# Foundation Scaffold Guardian

## Objective

Keep a reusable SaaS foundation coherent, product-agnostic, and independently buildable while allowing deliberate evolution.

## Workflow

1. Read repository instructions, architecture documentation, generator code, and current validation commands.
2. Identify the generated template payload separately from foundation development tooling.
3. Map the requested change to application, service, shared-package, tooling, or documentation ownership.
4. Reject product-specific names and business rules from reusable defaults.
5. Prefer additive, backward-safe changes unless the user explicitly requests a breaking release.
6. Update generator behavior, examples, and documentation together.
7. Generate at least one representative project and run its documented checks.

## Invariants

- Generated projects work without the agent toolkit.
- Shared packages do not absorb product business logic.
- Optional capabilities do not become hidden mandatory dependencies.
- The generator copies an explicit template payload, not repository development internals.
- Existing repository instructions take precedence over generic foundation preferences.

Read `../../core/policies/portability.md` when the change affects portability.
