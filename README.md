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

## Install in Codex

The recommended installation unit is the complete plugin. Do not install the skill directories individually: role skills reference shared contracts in `agents/` and `core/`.

### Public releases

Install a tagged release directly from GitHub:

```bash
codex plugin marketplace add timucintezcan/saas-agent-toolkit --ref v0.1.0
codex plugin add saas-agent-toolkit@saas-agent-toolkit
```

### Local development

Clone the repository, then run:

```bash
codex plugin marketplace add /absolute/path/to/saas-agent-toolkit
codex plugin add saas-agent-toolkit@saas-agent-toolkit
```

Start a new Codex task after installation so the newly installed skills are loaded.

Verify the installation with:

```bash
codex plugin list
```

The expected result is an enabled `saas-agent-toolkit` plugin containing eight specialist agent profiles and seventeen skills in version `0.1.0`.

## Using the Toolkit

Ask Codex for an outcome rather than selecting every skill manually. Examples:

- "Assess this repository for release readiness."
- "Prepare a preview-first Vercel deployment plan."
- "Review this Supabase schema and RLS model."
- "Define the environment contract without exposing secret values."
- "Coordinate the implementation of this multi-phase SaaS feature."

Codex should select the narrowest applicable skill or adopt the Delivery Orchestrator for cross-cutting work. Production mutations still require explicit approval.

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

## Validation

Run the portable repository validator and its tests:

```bash
python3 scripts/validate_repository.py
python3 -m unittest discover -s tests -p "test_*.py"
```

CI runs the same checks for pushes and pull requests. Maintainers should also run the canonical Codex skill and plugin validators before publishing a release.

See [`docs/releasing.md`](docs/releasing.md) for the release checklist.

## License

MIT
