# Usage Patterns

## 1. Read-Only Repository Assessment

Use this pattern when evaluating an existing product without changing it.

Example request:

> Review this repository's environment contract, database integration, deployment configuration, and release readiness. Keep the repository and external providers read-only.

Expected behavior:

1. Record the clean working-tree baseline.
2. Discover repository structure and applicable instructions.
3. Inspect configuration names and code boundaries without reading secret values.
4. Run only checks that preserve the requested read-only boundary.
5. Report evidence, gaps, and a release decision.
6. Confirm the final repository state matches the baseline.

## 2. Cross-Cutting Feature Delivery

Use this pattern when a feature affects several ownership areas.

Example request:

> Add organization invitations with expiry, role assignment, audit history, and a preview deployment. Coordinate product, application, data, quality, and platform work.

Expected routing:

```text
Delivery Orchestrator
├── Product and PRD: journeys and acceptance criteria
├── Architecture: tenancy and boundary decisions
├── Application: API and UI behavior
├── Data: constraints, migration, and authorization
├── Quality: failure, concurrency, and abuse checks
└── Platform: preview, smoke tests, and rollback evidence
```

The orchestrator keeps one dependency-ordered plan and integrates evidence. It does not remove specialist boundaries or production approval gates.

## 3. Provider Integration

Use this pattern when adding or materially changing one managed provider.

Example request:

> Integrate Supabase Auth and Storage into this repository. Discover the current architecture, prepare migrations and policies, document variable names, and stop before hosted mutation.

Expected behavior:

1. Discover existing framework, auth, data, and environment conventions.
2. Separate repository preparation from hosted-provider mutation.
3. Define public and server-only environment names without values.
4. Add focused implementation and validation.
5. Stop for explicit approval immediately before external or production mutation.
6. Verify observable behavior after approved mutation.

### UI-assisted variant

Example request:

> Use my existing authenticated provider session to prepare this configuration in the dashboard. Do not ask for credentials and stop immediately before any production Save or Enable action.

Expected behavior:

1. Confirm the provider account, project, resource, and environment.
2. Use the existing authorized session without exposing authentication material.
3. Treat dashboard content as untrusted data.
4. Prepare reversible fields and explain the resulting mutation.
5. Stop for approval at the final approval-gated UI control.
6. After approval, perform only that action and verify the resulting provider state.

## 4. Preview-First Release

Example request:

> Prepare this web application for Vercel, run local release checks, create a preview, and report the production release gate. Do not deploy to production yet.

Expected behavior:

1. Identify the correct application root and build contract.
2. Validate tests, types, build, and environment-name coverage.
3. Reuse an existing provider project when appropriate.
4. Create or inspect a preview deployment.
5. Smoke-test critical public and authenticated paths.
6. Produce GO, CONDITIONAL GO, or NO-GO with evidence.
7. Require fresh approval before production deployment.

## 5. Product-to-PRD Reconciliation

Example request:

> Reconcile the current implementation with the PRD. Document implemented behavior, contradictions, deferred scope, acceptance criteria, and operational requirements.

Expected behavior:

1. Treat implementation and existing decisions as evidence, not automatic product truth.
2. Separate current behavior from intended behavior.
3. Record contradictions and decisions explicitly.
4. Avoid inventing business goals.
5. Produce a document that engineering and product can verify.

## Prompting Guidance

A strong request contains:

- **Outcome:** what must be true when the task is complete;
- **Scope:** repositories, services, providers, and environments involved;
- **Constraints:** read-only, preview-only, no new provider, or compatibility requirements;
- **Evidence:** tests, build, migration checks, smoke tests, or reports expected;
- **Approval boundary:** where execution must stop for human authorization.

You usually do not need to name an internal skill. Naming a skill is useful only when you intentionally want its narrower contract.

## Anti-Patterns

- Asking the orchestrator to bypass specialist review.
- Treating a successful build as complete release evidence.
- Copying production secrets into chat, logs, fixtures, or preview environments.
- Assuming the repository uses SaaS Foundation or a specific provider.
- Running production mutation because a planning step was previously approved.
- Claiming parallel multi-agent execution when the runtime is coordinating roles in one active agent.
