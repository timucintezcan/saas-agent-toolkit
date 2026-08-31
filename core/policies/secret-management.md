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

## Interactive Authentication

- Ask the user to authenticate directly in the provider UI when an interactive login, MFA, recovery, CAPTCHA, consent, or password-manager step is required.
- Use an existing authorized browser session without attempting to reveal, copy, export, or persist its credentials.
- Do not inspect hidden secret fields, browser storage, clipboard contents, password-manager records, recovery codes, or authentication cookies.
- Treat masked values as secrets even when their full value is not visible.
- Capture screenshots or provider evidence only when needed, and exclude or redact sensitive account and personal information.

## Environment Separation

Development, preview, staging, and production may use different credentials. A skill must identify the target environment before changing configuration.
