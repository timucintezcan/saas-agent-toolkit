# Architecture

## Objective

SaaS Agent Toolkit separates durable engineering knowledge from coding-agent-specific packaging.

## Layers

### Core

`core/` is the vendor-neutral source of truth for roles, workflows, and safety policies. Core documents describe outcomes and invariants without depending on Codex, Claude Code, or a specific model.

### Skills

`skills/` contains bounded Codex skills. A skill may apply a core workflow, add provider-specific guidance, and use deterministic scripts. Skills should remain independently discoverable and avoid loading unrelated references.

### Future Adapters

Codex is the reference implementation in `0.1.x`. A Claude Code adapter will consume the same core contracts after those contracts have been validated. Adapter-specific files must not become a second source of business rules.

## Dependency Direction

```text
adapter skill -> core workflow or policy
provider skill -> shared provider-neutral contract
core -> no adapter dependency
```

SaaS Foundation and user applications are test targets, not dependencies.

## Portability

Skills must work with:

1. projects generated from SaaS Foundation;
2. existing SaaS repositories with different layouts;
3. repositories that use only a subset of supported providers.

Every skill starts with repository discovery and preserves existing architectural choices unless the user explicitly requests a change.
