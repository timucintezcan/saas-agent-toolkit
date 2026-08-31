# Claude Code Adapter

This adapter lets Claude Code load the toolkit's shared skills without creating a second source of truth.

## Local development

From a checkout of this repository, start Claude Code with the repository as a plugin directory:

```bash
claude --plugin-dir /path/to/saas-agent-toolkit
```

Claude Code discovers the root `.claude-plugin/plugin.json` and the root `skills/` directory. Skills are namespaced as `/saas-agent-toolkit:<skill-name>`.

Reload after editing with `/reload-plugins`.

## Operating contract

- `core/` remains the vendor-neutral source of truth.
- `agents/` remains the durable outcome and delegation model.
- `skills/` is loaded natively by Claude Code; it is not copied or rewritten.
- Claude Code may use the same provider, approval, secret-management, and release contracts as Codex.
- Human approval is still required immediately before production mutations.

The adapter intentionally does not add provider credentials, MCP servers, hooks, or model-specific prompt copies. Add those only when a concrete Claude Code capability requires them and document the boundary here first.
