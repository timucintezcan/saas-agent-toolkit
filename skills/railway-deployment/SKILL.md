---
name: railway-deployment
description: Prepare, deploy, verify, and document SaaS APIs, workers, scheduled jobs, and supporting services on Railway. Use for Railway project, service, environment, domain, or production release work.
---

# Railway Deployment

## Objective

Deploy the correct backend or worker components to Railway with explicit service boundaries, health checks, variables, migration order, observation, and rollback.

## Workflow

1. Discover services, start commands, ports, health endpoints, Docker or native build configuration, persistent storage, jobs, and database dependencies.
2. Verify current CLI and platform behavior using official Railway documentation or installed CLI help.
3. Identify the existing Railway project, environment, and services before creating resources.
4. Separate API, worker, migration, and scheduled-job responsibilities; do not run a worker inside a web process by accident.
5. Define variable references and environment scope without printing secret values.
6. Run local build, test, startup, and health checks.
7. Prepare migration and deployment order, including how a failed migration or incompatible release is contained.
8. Use a non-production environment when available and verify logs, health, networking, and dependency connectivity.
9. Request explicit approval before creating paid resources, mutating Production, adding domains, changing secrets, or applying production migrations.
10. Record deployment identifiers, health evidence, and rollback or redeploy steps.

## Safety

- Do not expose private service ports or databases publicly without a requirement.
- Do not assume ephemeral filesystems are durable.
- Do not run destructive migrations automatically on every process start.
- Do not report success while the service is restarting, unhealthy, or missing worker execution.

Apply `../../core/policies/approval-gates.md`, `../../core/policies/secret-management.md`, `../../core/workflows/provider-integration.md`, and `../../core/workflows/release-lifecycle.md`.
