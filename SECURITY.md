# Security Policy

## Reporting a Vulnerability

Do not open a public issue for a sensitive vulnerability. Use GitHub Security Advisories for private disclosure.

## Secret Handling

- Never commit API keys, tokens, private keys, credentials, or production environment files.
- Skills must reason about environment variable names, not request secret values in chat.
- Scripts must not print secret values.
- Rotate a credential at its provider if exposure is suspected; removing it from Git is not sufficient.

## Production Operations

Production deployment, migration, DNS, billing, secret, and destructive data operations require explicit human approval immediately before execution.
