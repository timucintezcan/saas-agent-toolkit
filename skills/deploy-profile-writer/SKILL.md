---
name: deploy-profile-writer
description: Design a managed-service deployment profile and release order for a SaaS repository. Use when choosing or documenting web, API, worker, database, queue, storage, DNS, and observability targets.
---

# Deploy Profile Writer

## Objective

Create a provider-aware deployment profile that minimizes operational overhead and keeps preview, production, migration, secrets, verification, and rollback explicit.

## Discovery

Identify:

- applications, services, workers, scheduled jobs, and health endpoints;
- runtime and region constraints;
- database, queue, storage, authentication, and third-party dependencies;
- existing providers and deployment configuration;
- environment-variable names and ownership;
- migration and rollback requirements.

## Output

Document:

1. component-to-provider mapping;
2. environment and region topology;
3. build, migration, and deployment order;
4. environment-variable names grouped by component and sensitivity;
5. preview and production verification;
6. health checks and operational signals;
7. rollback and recovery path;
8. unsupported assumptions and open decisions.

## Constraints

- Prefer managed services proportional to product scale.
- Do not introduce a separate service when the existing runtime safely supports the workload.
- Do not include secret values.
- Do not perform production mutation as part of profile writing.
- Apply `../../core/policies/approval-gates.md`, `../../core/policies/secret-management.md`, and `../../core/workflows/release-lifecycle.md`.
