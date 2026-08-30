# Agent Model

## Definitions

- **Agent profile:** Vendor-neutral responsibility, decision boundary, and output contract stored in `agents/`.
- **Role:** Durable engineering responsibilities stored in `core/roles/`.
- **Skill:** A bounded, discoverable procedure exposed by an adapter.
- **Adapter:** Packaging that makes profiles and skills usable in a specific coding agent.
- **Tool:** A deterministic execution primitive such as a CLI, API, script, or MCP server.

## Current Runtime Model

Codex is the reference adapter. Specialist agent profiles are exposed as Codex role skills. Invoking a role skill makes the current Codex agent adopt that profile and select narrower skills as needed.

This is coordinated role execution, not a claim that every profile runs as an independent parallel process. True parallel multi-agent execution requires a supporting runtime and will be evaluated separately after the role contracts are stable.

## Source of Truth

```text
core roles and policies
        ↓
agent profiles
        ↓
Codex role skills
        ↓
provider and workflow skills
```

Adapter files must remain thin. Shared rules belong in `core/`; outcome ownership belongs in `agents/`; provider mechanics belong in focused skills.
