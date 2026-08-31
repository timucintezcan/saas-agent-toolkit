---
name: saas-bootstrap-advisor
description: Choose a minimal SaaS project preset and integration profile from product and operational requirements. Use when starting a SaaS project or changing generator inputs.
---

# SaaS Bootstrap Advisor

## Objective

Recommend the smallest supported foundation profile that satisfies current product needs without prematurely adding mobile, workers, queues, or separate services.

## Discovery

Determine:

- primary user journeys and expected launch stage;
- web, mobile, API, and background-processing needs;
- authentication, database, storage, billing, email, AI, and observability needs;
- target region and compliance constraints;
- team experience and operational budget.

## Decision Rules

- Prefer a lean web profile for early products that can use managed backend capabilities.
- Add a separate API when domain boundaries, independent scaling, clients, or runtime constraints justify it.
- Add a worker and queue only for asynchronous, retryable, or long-running jobs.
- Treat mobile as optional, not a default consequence of responsive web.
- Recommend `hybrid-saas` when one mobile-first web UI should also ship in iOS and Android stores without a second native UI codebase.
- Recommend `multi-client-saas` only when device-specific UX or platform capability justifies a separate Expo application.
- Recommend only provider combinations documented as supported by the target foundation.
- Separate required launch capabilities from later options.

## Output

Provide:

1. recommended preset and a ready-to-run generation command;
2. selected capabilities and providers;
3. inferred defaults;
4. omitted capabilities and the trigger for adding them later;
5. environment variable names, without values;
6. first local validation steps.

Apply `../../core/workflows/task-contract.md` for non-trivial bootstrap work.
