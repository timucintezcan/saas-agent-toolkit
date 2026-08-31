# SaaS Agent Toolkit

[![Validate toolkit](https://github.com/timucintezcan/saas-agent-toolkit/actions/workflows/validate.yml/badge.svg)](https://github.com/timucintezcan/saas-agent-toolkit/actions/workflows/validate.yml)
[![GitHub release](https://img.shields.io/github/v/release/timucintezcan/saas-agent-toolkit)](https://github.com/timucintezcan/saas-agent-toolkit/releases/latest)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Reusable agent profiles, Codex and Claude Code adapters, delivery workflows, and production safety policies for building and operating SaaS products.

The toolkit is product-agnostic and repository-aware. It works with projects generated from [SaaS Foundation](https://github.com/timucintezcan/saas-foundation) and with existing repositories that use different frameworks or providers.

## Why This Exists

Coding agents are useful, but repeatable SaaS delivery needs more than prompts. It needs explicit ownership, bounded procedures, evidence-based validation, and human approval at production boundaries.

SaaS Agent Toolkit provides those reusable contracts:

- **Agent profiles** own outcomes such as product definition, architecture, data, release, and quality.
- **Skills** execute focused procedures such as Supabase integration, Vercel deployment, or release assessment.
- **Core workflows and policies** keep safety, portability, and approval rules consistent.
- **Validation tooling** checks repository structure, skill metadata, marketplace packaging, and documentation links.

## What It Is — and Is Not

| It is | It is not |
| --- | --- |
| A reusable engineering control plane for SaaS work | A generated SaaS application |
| A coordinated role-and-skill model | A claim of independent parallel agents |
| Repository-aware and provider-conscious | Coupled to one framework or cloud |
| Preview-first and evidence-driven | Permission to mutate production automatically |
| Compatible with SaaS Foundation | Dependent on SaaS Foundation |

## Install and Use

Install the toolkit once in the agent environment, then use it with any compatible SaaS repository. It is not a dependency that you copy into each product repository.

### Codex

Install the current stable release:

```bash
codex plugin marketplace add timucintezcan/saas-agent-toolkit --ref v0.2.0
codex plugin add saas-agent-toolkit@saas-agent-toolkit
```

Start a new Codex task so the installed skills are loaded, then verify the plugin:

```bash
codex plugin list
```

### Claude Code

Clone the tagged release to a trusted local location, then load it as a plugin directory for the session:

```bash
git clone --branch v0.2.0 --depth 1 https://github.com/timucintezcan/saas-agent-toolkit.git ~/Developer/saas-agent-toolkit
claude --plugin-dir ~/Developer/saas-agent-toolkit
```

Claude Code exposes shared skills as `/saas-agent-toolkit:<skill-name>` and specialist subagents as `@saas-agent-toolkit:<agent-name>`.

### First Request

Start with an outcome and constraints rather than naming every internal skill:

> Assess this repository for release readiness. Do not mutate production resources.

Choose one platform as the primary writer for a task. Use the other platform for an independent review only when it will not edit the same working tree concurrently.

See [Getting Started](docs/getting-started.md) and [Agent Platform Adapters](docs/adapters.md) for installation, upgrades, and platform boundaries.

## How It Works

```text
User objective
      ↓
Delivery Orchestrator or narrow specialist
      ↓
Agent outcome contract
      ↓
Focused workflow or provider skill
      ↓
Tools, repository changes, and verification evidence
      ↓
Human approval before production mutation
```

Codex selects the narrowest suitable skill. Claude Code can use the same skills and delegate to the specialist subagents. Cross-cutting objectives use the Delivery Orchestrator, which coordinates specialist responsibilities and approval gates without pretending that every profile runs as an independent process.

Read [Agent Model](docs/agent-model.md) for the execution and routing contract.

## Specialist Agents

| Agent | Primary ownership |
| --- | --- |
| Delivery Orchestrator | Cross-cutting plans, dependencies, routing, and integrated evidence |
| Product and PRD | Product intent, MVP scope, journeys, acceptance criteria, and decision records |
| Architecture | System, repository, service, API, data, and deployment boundaries |
| Application Engineering | Frontend, backend, API, authentication, and integration implementation |
| Data and Database | Schemas, migrations, authorization, concurrency, retention, and query performance |
| Platform and Release | Environments, CI/CD, managed infrastructure, deployments, domains, and rollback |
| Quality and Security | Test strategy, security, privacy, resilience, and independent release decisions |
| Observability and Cost | Logs, metrics, alerts, performance, incidents, and provider cost signals |

## Skill Coverage

The current repository contains 22 skills across four groups:

- **Role adapters:** delivery, product, architecture, application, data, platform, quality, and observability.
- **Provider integrations:** Supabase, Vercel, Railway, OpenAI, Cloudflare, Sentry, Resend, and Stripe.
- **Environment and release:** environment contracts, deployment profiles, and release readiness.
- **Foundation workflows:** SaaS bootstrap decisions and scaffold protection.

See the [Skill Catalog](docs/skill-catalog.md) for activation guidance for every skill.

## Roadmap Principles

The toolkit adds skills only after repeated real-project needs demonstrate a stable workflow. Current candidates include GitHub CI/CD delivery, Playwright-based end-to-end browser quality, and a TypeScript/Next.js/Supabase SaaS security review. They are documented as roadmap candidates, not current compatibility promises. See [Planned Skills](docs/skill-catalog.md#planned-skills).

## Safety Model

Repository discovery and read-only inspection can proceed without mutation approval. Explicit human approval is required immediately before:

- production deployment;
- production migration or backfill;
- DNS, domain, or OAuth callback mutation;
- secret creation, rotation, or revocation;
- destructive data operations;
- billing or paid-resource changes.

The toolkit never treats an earlier planning approval as authorization for a later production mutation. See [Approval Gates](core/policies/approval-gates.md) and [Secret Management](core/policies/secret-management.md).

## Repository Map

```text
.agents/plugins/      Git and local Codex marketplace entry
.codex-plugin/        Codex plugin manifest
.claude-plugin/       Claude Code plugin manifest
adapters/             Platform-specific loading guidance
agents/               Specialist outcome contracts and Claude subagent metadata
core/roles/           Durable engineering responsibilities
core/workflows/       Shared task, provider, agent, and release workflows
core/policies/        Approval, secret, and portability rules
skills/               Discoverable Codex role and procedure adapters
scripts/              Deterministic repository validators
tests/                Validator behavior tests
docs/                 Architecture, usage, catalog, and release guides
```

Read [Architecture](docs/architecture.md) for dependency direction and extension boundaries.

## Documentation

- [Getting Started](docs/getting-started.md)
- [Skill Catalog](docs/skill-catalog.md)
- [Usage Patterns](docs/usage-patterns.md)
- [Agent Model](docs/agent-model.md)
- [Agent Platform Adapters](docs/adapters.md)
- [Architecture](docs/architecture.md)
- [Provider Skills](docs/provider-skills.md)
- [Release Process](docs/releasing.md)
- [Contributing](CONTRIBUTING.md)
- [Security Policy](SECURITY.md)

## Project Status

`v0.2.0` is the current stable release. It supports Codex skills plus Claude Code skills and specialist subagents, and adds Cloudflare, Sentry, Resend, and Stripe provider skills with shared UI-assisted provider execution. See `docs/adapters.md` for platform boundaries.

## Validation

```bash
python3 scripts/validate_repository.py
python3 -m unittest discover -s tests -p "test_*.py"
```

CI runs the same checks for pushes and pull requests. Releases additionally require canonical Codex skill and plugin validation plus clean marketplace installation evidence.

## License

[MIT](LICENSE)
