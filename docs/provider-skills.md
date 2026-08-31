# Provider Skills

Provider skills implement bounded integration and operation workflows. They do not decide product scope or replace application, data, platform, security, or observability ownership.

## Current Provider Pack

| Skill | Coverage |
| --- | --- |
| `supabase-project-setup` | Database, Auth, Storage, migrations, RLS, and generated types |
| `vercel-deployment` | Web projects, environments, previews, domains, production release, and rollback evidence |
| `railway-deployment` | APIs, workers, scheduled jobs, services, environments, domains, and releases |
| `openai-integration` | Server-side API integration, structured output, evaluations, retries, cost controls, and fallback |
| `cloudflare-domain-operations` | Zones, DNS, proxy, TLS, redirects, caching, basic edge security, and domain verification |
| `sentry-observability-setup` | Error capture, releases, source maps, tracing, sampling, privacy, alerts, and controlled-event verification |
| `resend-email-integration` | Transactional email, sending domains, templates, idempotency, retries, webhooks, and delivery verification |

Environment and deployment support is provided by `environment-contract-manager` and `deploy-profile-writer`. See the complete [Skill Catalog](skill-catalog.md).

## Provider Lifecycle

Every provider workflow follows the same control sequence:

1. **Discover:** identify current repository structure, provider configuration, environments, and ownership.
2. **Verify currency:** consult current official documentation or installed CLI help when behavior may have changed.
3. **Prepare:** make focused repository changes and document environment-variable names without values.
4. **Validate locally:** run tests, type checks, builds, migration checks, or dry-runs appropriate to the integration.
5. **Preview:** use preview or non-production state when the provider supports it.
6. **Approve:** request explicit human approval immediately before external production mutation.
7. **Mutate:** perform only the approved operation with the narrowest practical scope.
8. **Verify:** collect immutable identifiers, health checks, smoke tests, policy checks, or usage evidence.
9. **Handoff:** record rollback, remaining risks, and operational ownership.

## Documentation Policy

Provider interfaces, pricing, limits, CLI commands, and dashboard navigation change over time. Provider skills store durable decisions and invariants rather than copied provider manuals.

When exact behavior matters, use current official provider documentation or installed CLI help. Clearly distinguish verified behavior from inference.

## Mutation Policy

Repository preparation may proceed after the task is clear. External project creation, production deployment, domain changes, OAuth callback changes, secret operations, destructive operations, and paid-resource changes require explicit human approval immediately before mutation.

Provider skills must avoid duplicate projects, services, domains, and credentials by discovering existing provider state first.

## Verification Standard

A successful command is not sufficient evidence. Provider work should verify the user-visible or operational outcome, such as:

- deployment URL and critical-route smoke tests;
- migration state and authorization behavior;
- health, logs, and rollback reference;
- model output contract and fallback behavior;
- environment scope without exposing values.

## Adding a Provider Skill

A new provider skill must:

- solve a repeated provider-specific task;
- define repository and external-state discovery;
- reference shared approval, secret, and provider workflows;
- separate preparation, preview, and production mutation;
- define verification, rollback, failure, and stopping behavior;
- avoid requiring the provider for unrelated toolkit functionality;
- pass skill, plugin, repository, and behavioral validation.

Stripe is the next planned candidate. Further providers depend on repeated SaaS demand and real-project validation, not provider popularity alone.
