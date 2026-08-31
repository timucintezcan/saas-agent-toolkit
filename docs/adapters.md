# Agent Platform Adapters

The toolkit keeps reusable engineering rules platform-neutral and exposes them through thin platform adapters.

## Supported adapters

### Codex

Codex is the reference adapter. Install the repository plugin through the local marketplace entry in `.agents/plugins/marketplace.json`. Codex skill metadata lives beside each skill in `skills/<skill>/agents/openai.yaml`.

### Claude Code

Claude Code is supported through the root `.claude-plugin/plugin.json` and the same root `skills/` directories. For local development:

```bash
claude --plugin-dir /path/to/saas-agent-toolkit
```

The adapter exposes namespaced skills such as `/saas-agent-toolkit:product-prd` and native subagents such as `@saas-agent-toolkit:product-prd`. Claude Code uses each skill's `SKILL.md`; Codex-only `agents/openai.yaml` metadata is ignored by Claude Code.

## Source-of-truth rules

- Put durable rules, safety boundaries, and output contracts in `core/`.
- Put outcome ownership and delegation in `agents/`.
- Put platform-specific loading or invocation instructions in this document or `adapters/`.
- Do not fork a skill into separate Codex and Claude copies.
- When an adapter needs different behavior, document the smallest compatibility layer and preserve the shared contract.

## Foundation projects

SaaS Foundation generates project-local `AGENTS.md`, `CLAUDE.md`, and operational contracts. Those files govern the generated product repository. The toolkit is optional and should be loaded separately by the selected agent platform.
