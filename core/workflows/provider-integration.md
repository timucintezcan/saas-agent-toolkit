# Provider Integration Workflow

## 1. Discover

Identify the target repository, component, environment, existing provider configuration, package manager, deployment topology, and repository instructions.

## 2. Confirm Capability Need

State the product or operational capability the provider must supply. Do not add a provider because it is common or available.

## 3. Verify Current Provider Contract

Use current official provider documentation or installed CLI help for unstable setup details. Do not rely on remembered dashboard labels, pricing, limits, or deprecated commands.

## 4. Define the Environment Contract

List variable names, scope, sensitivity, owner, consumers, and target environments. Never request or print secret values.

## 5. Prepare Repository Changes

Add the smallest provider adapter, configuration, tests, and runbook required by the capability. Keep provider code replaceable and isolate SDK-specific behavior.

## 6. Validate Locally or in Preview

Run focused tests, build checks, configuration validation, and a preview or dry-run when available.

## 7. Request Mutation Approval

Before creating or changing an external project, production environment, domain, secret, paid resource, or deployment, state the exact mutation, cost risk, verification, and rollback.

## 8. Verify and Record

Capture non-secret identifiers, immutable deployment references, health evidence, and the recovery path. Update the project runbook without copying secrets.
