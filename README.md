# SaaS Agent Toolkit

Reusable agent roles, skills, workflows, and safety policies for building and operating SaaS products.

The toolkit is product-agnostic and repository-aware. It can support projects generated from [SaaS Foundation](https://github.com/timucintezcan/saas-foundation) as well as existing SaaS codebases with different structures.

## Project Status

This repository is in its initial `0.1.x` development phase. Codex is the reference adapter. A Claude Code adapter will be added after the shared workflows have been validated against real projects.

## Design Principles

- Keep shared engineering knowledge vendor-neutral.
- Treat agents as owners of outcomes and skills as bounded reusable procedures.
- Discover the target repository before prescribing changes.
- Never require SaaS Foundation to use the toolkit.
- Keep provider-specific behavior behind focused skills.
- Require explicit human approval for production mutations.
- Never expose, print, or commit secret values.
- Validate observable outcomes instead of generated wording.

## Repository Structure

```text
.codex-plugin/       Codex plugin manifest
core/roles/          Vendor-neutral agent responsibilities
core/workflows/      Shared delivery contracts
core/policies/       Safety, portability, and approval rules
agents/              Executable specialist profile contracts
skills/              Discoverable Codex skills
docs/                Architecture and contributor documentation
```

## Initial Skills

- `foundation-scaffold-guardian`
- `saas-bootstrap-advisor`
- `release-readiness-checker`
- `deploy-profile-writer`

## Specialist Agents

- Delivery Orchestrator
- Product and PRD Agent
- Architecture Agent
- Application Engineering Agent
- Data and Database Agent
- Platform and Release Agent
- Quality and Security Agent
- Observability and Cost Agent

Each profile has a corresponding Codex role skill. These adapters let the current Codex agent adopt a specialist outcome contract and select narrower workflow or provider skills. See [`docs/agent-model.md`](docs/agent-model.md).

Initial provider and configuration skills:

- `environment-contract-manager`
- `supabase-project-setup`
- `vercel-deployment`
- `railway-deployment`
- `openai-integration`

Cloudflare, Stripe, Resend, and Sentry skills will be added incrementally after the initial pack is validated against real projects. See [`docs/provider-skills.md`](docs/provider-skills.md).

## Relationship to SaaS Foundation

```text
SaaS Foundation      creates application code
SaaS Agent Toolkit   plans, reviews, integrates, validates, and releases it
```

The repositories have independent release cycles. Generated applications must remain buildable, testable, and deployable without an installed AI agent.

## Safety Model

The toolkit may prepare and validate production changes, but it must request explicit approval immediately before:

- production deployment;
- production database migration or backfill;
- DNS, domain, or OAuth callback mutation;
- secret creation, rotation, or revocation;
- destructive data operations;
- billing or paid-provider changes.

Read [`core/policies/approval-gates.md`](core/policies/approval-gates.md) for the full contract.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). Skills must remain product-agnostic, include clear activation boundaries, and define verification and stopping conditions.

## License

MIT
