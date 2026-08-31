---
name: sentry-observability-setup
description: Integrate and verify Sentry error, release, source-map, tracing, alert, and privacy controls for SaaS applications. Use for new Sentry setup or material observability changes.
---

# Sentry Observability Setup

## Objective

Create actionable, privacy-conscious Sentry signals that identify user-impacting failures and connect them to environments, releases, owners, and deploys.

## Workflow

1. Define the operational decisions Sentry must support: affected runtime, user impact, ownership, release regression, performance bottleneck, or incident response.
2. Discover application runtimes, framework boundaries, deployment environments, current telemetry, release identifiers, source-map build flow, alert ownership, and any existing Sentry organization or project.
3. Verify current SDK setup, CLI commands, source-map behavior, and platform limits using official Sentry documentation or installed CLI help.
4. Reuse the correct existing organization and project when appropriate; avoid duplicate projects and fragmented environment names.
5. Classify configuration by exposure. A client DSN may be public by design, while auth tokens and organization automation credentials remain build-time or server-only secrets.
6. Initialize only the required browser, server, edge, mobile, worker, or job runtimes. Set stable environment and release identifiers across build, deploy, and runtime boundaries.
7. Upload source maps through the approved build path and prevent unintended public source exposure. Verify symbolication rather than assuming upload success.
8. Configure error filtering, data scrubbing, trace or profile sampling, and user context proportionally to diagnostic value, traffic, privacy obligations, and cost.
9. Define actionable alerts with an owner and response expectation. Avoid alerts that cannot trigger a decision.
10. Request explicit approval before creating external projects, adding credentials, enabling production telemetry, changing production sampling materially, creating alerts, or mutating provider-side retention and privacy settings.
11. Trigger a controlled non-production test error and, when applicable, a trace. Verify event ingestion, environment, release, symbolication, tags, scrubbing, grouping, and alert routing.

## Safety

- Do not enable default personal-data collection without an explicit purpose and privacy review.
- Do not log secrets, authorization headers, request bodies, session tokens, or unnecessary user content.
- Do not delete events, reset reports, disable alerts, or lower privacy controls without approval.
- Do not report completion from SDK compilation alone; verify a real controlled event.
- Coordinate with existing OpenTelemetry or monitoring architecture instead of duplicating telemetry blindly.

## Output

Report runtime coverage, environment and release mapping, secret-name contract, privacy and sampling decisions, controlled-event evidence, alert ownership, cost risks, and rollback or disable instructions.

Apply `../../core/policies/approval-gates.md`, `../../core/policies/secret-management.md`, `../../core/workflows/provider-integration.md`, and `../../core/roles/observability-cost.md`.
