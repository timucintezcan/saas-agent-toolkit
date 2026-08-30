# Skill Catalog

Skills are bounded procedures or role adapters. Ask for the desired outcome; Codex should activate the narrowest matching skill and use the Delivery Orchestrator only when the objective crosses ownership boundaries.

## Specialist Role Adapters

| Skill | Use when |
| --- | --- |
| `saas-delivery-orchestrator` | A multi-phase objective spans product, application, data, platform, quality, or observability work. |
| `saas-product-agent` | Product intent, PRD scope, user journeys, acceptance criteria, or product decisions need clarification. |
| `saas-architecture-agent` | System, repository, service, API, data, deployment, or scalability boundaries require consequential decisions. |
| `saas-application-agent` | Frontend, backend, API, authentication, or integration behavior must be implemented within the existing architecture. |
| `saas-data-agent` | Schema, migration, RLS, authorization, transaction, concurrency, retention, or query-performance work is required. |
| `saas-platform-agent` | Environments, infrastructure, CI/CD, deployments, domains, release order, smoke tests, or rollback are central. |
| `saas-quality-agent` | Test strategy, security, privacy, resilience, abuse cases, or an independent release decision is needed. |
| `saas-observability-agent` | Logging, metrics, alerts, SLOs, performance, incidents, AI usage, storage growth, or provider cost must be assessed. |

## Provider and Integration Skills

| Skill | Use when |
| --- | --- |
| `supabase-project-setup` | Integrating or materially changing Supabase Database, Auth, Storage, migrations, RLS, or generated types. |
| `vercel-deployment` | Preparing or operating preview-first Vercel web deployment, domains, environment scope, smoke tests, or rollback. |
| `railway-deployment` | Preparing or operating Railway APIs, workers, scheduled jobs, services, environments, domains, or releases. |
| `openai-integration` | Designing or changing an OpenAI feature with server-side secrets, structured output, evaluations, retries, cost controls, and fallback. |

## Environment and Release Skills

| Skill | Use when |
| --- | --- |
| `environment-contract-manager` | Discovering, classifying, documenting, or validating environment-variable names without exposing values. |
| `deploy-profile-writer` | Selecting and documenting managed targets for web, API, worker, database, queue, storage, DNS, and observability. |
| `release-readiness-checker` | Producing an evidence-based GO, CONDITIONAL GO, or NO-GO decision before preview, production, tagging, or public release. |

## Foundation Skills

| Skill | Use when |
| --- | --- |
| `saas-bootstrap-advisor` | Choosing a minimal SaaS project preset and integration profile from product and operational requirements. |
| `foundation-scaffold-guardian` | Protecting a reusable SaaS foundation from product-specific drift or unsafe generator and workspace changes. |

## Selection Rules

1. Prefer one narrow skill when one skill owns the outcome.
2. Use a specialist role when judgment spans several related procedures in one discipline.
3. Use the Delivery Orchestrator when dependencies cross specialist boundaries.
4. Keep one integrated plan and one final evidence summary.
5. Never delegate production authorization to another agent or skill.

## Planned Skills

Cloudflare, Stripe, Resend, and Sentry are planned after the initial provider contracts receive additional real-project evaluation. Planned work is not part of the current compatibility promise.
