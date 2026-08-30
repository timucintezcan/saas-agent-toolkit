# Portability Policy

## Repository Discovery

Before prescribing changes, identify:

- repository type and workspace boundaries;
- package manager and runtime versions;
- frameworks and build commands;
- current deployment providers;
- environment variable contract;
- database and migration system;
- existing instructions and contribution rules;
- available tests and validation commands.

## Constraints

- Do not assume SaaS Foundation paths.
- Do not require unused services or providers.
- Do not replace an existing architecture without explicit user intent.
- Prefer capability detection over provider-name guessing.
- Keep provider adapters replaceable.
- Produce artifacts that remain usable without an installed AI agent.
