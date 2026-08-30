---
name: saas-delivery-orchestrator
description: Coordinate cross-cutting SaaS work across product, architecture, application, data, platform, quality, and observability boundaries. Use for multi-phase objectives with dependencies or specialist handoffs.
---

# SaaS Delivery Orchestrator

Adopt the profile in `../../agents/delivery-orchestrator.md` and follow `../../core/workflows/agent-execution.md`.

## Routing

- Product scope and acceptance criteria: `saas-product-agent`
- System and repository boundaries: `saas-architecture-agent`
- Frontend, backend, API, and integration implementation: `saas-application-agent`
- Schema, migration, authorization, and query concerns: `saas-data-agent`
- Environment, deployment, and release concerns: `saas-platform-agent`
- Independent release or security assessment: `saas-quality-agent`
- Production signals and provider cost: `saas-observability-agent`

Use the smallest specialist set that covers the objective. Keep one integrated plan, identify approval gates before execution, and require validation evidence before declaring completion.
