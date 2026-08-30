# Security Policy

## Supported Versions

Security fixes are applied to the latest released minor line. Users should install a tagged release and review release notes before upgrading.

| Version | Supported |
| --- | --- |
| `0.1.x` | Yes |
| Unreleased development commits | Best effort |

## Reporting a Vulnerability

Do not open a public issue for a sensitive vulnerability. Use [GitHub Security Advisories](https://github.com/timucintezcan/saas-agent-toolkit/security/advisories/new) for private disclosure.

Include:

- affected release or commit;
- affected agent, skill, policy, script, or packaging path;
- reproduction steps or a minimal example;
- realistic impact and required permissions;
- any known mitigation.

Do not include real credentials, private repository contents, personal data, or production records in the report.

## Security Scope

Relevant findings include:

- secret-value exposure through prompts, logs, fixtures, or scripts;
- approval-gate bypass for production or external mutation;
- unsafe default behavior that can destroy or disclose data;
- prompt-injection paths that override repository or safety instructions;
- tenant-isolation, authorization, or migration guidance that creates a repeatable unsafe pattern;
- marketplace or plugin packaging that loads unintended files;
- deterministic scripts that execute beyond their documented scope.

Product-specific vulnerabilities in a target SaaS application should be reported to that product unless the toolkit created a reusable unsafe pattern.

## Secret Handling

- Never commit API keys, tokens, private keys, credentials, or production environment files.
- Skills reason about environment-variable names and ownership, not secret values.
- Scripts must not print secret values.
- Example files use placeholders only.
- Rotate a credential at its provider if exposure is suspected; removing it from Git is not sufficient.

## Production Operations

Production deployment, migration, DNS, billing, secret, and destructive-data operations require explicit human approval immediately before execution.

An approval to plan, prepare, preview, or validate an operation is not approval to execute the later production mutation.

## User Responsibilities

- Review repository changes before applying them.
- Keep provider credentials in approved secret stores.
- Use least-privilege provider identities.
- Prefer tagged toolkit releases over arbitrary development commits.
- Verify backups, rollback, and smoke-test plans before production changes.
- Treat generated guidance as input to engineering judgment, not as a replacement for provider permissions or organizational controls.
