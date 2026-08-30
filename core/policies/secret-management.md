# Secret Management

## Contract

- Work with secret names and ownership, not secret values.
- Never request that a user paste a secret into chat, source code, documentation, an issue, or a commit.
- Keep server-only credentials out of browser and mobile bundles.
- Store local secrets in ignored environment files or an approved secret manager.
- Store hosted secrets in the provider's environment or secret-management system.
- Verify presence and scope without printing values.
- Treat logs, screenshots, command history, and generated artifacts as potential disclosure channels.
- Rotate exposed credentials at the provider and review access logs.

## Environment Separation

Development, preview, staging, and production may use different credentials. A skill must identify the target environment before changing configuration.
