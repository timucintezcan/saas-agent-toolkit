---
name: environment-contract-manager
description: Discover, classify, document, and validate environment variables across local, preview, staging, and production environments without exposing values. Use for provider integration, deployment preparation, or secret hygiene.
---

# Environment Contract Manager

## Objective

Create an environment contract that tells people and automation which variables exist, where they are consumed, who owns them, and whether they are public, server-only, secret, or generated.

## Workflow

1. Read repository instructions, environment examples, runtime configuration, CI, deployment files, and provider adapters.
2. Extract variable names without reading or printing values unnecessarily.
3. Classify each variable by consumer, environment, sensitivity, source, requirement, and rotation owner.
4. Detect public-prefix misuse, duplicated meanings, stale names, missing examples, and server secrets referenced by client bundles.
5. Update `.env.example`, typed configuration, validation, and runbook documentation when requested.
6. Verify builds and tests with safe placeholder values or provider-approved local credentials.

## Output

Return a table with variable name, consumers, environments, classification, owner/source, required status, and validation. Report missing or unsafe configuration without exposing values.

Apply `../../core/policies/secret-management.md`, `../../core/policies/portability.md`, and `../../core/workflows/provider-integration.md`.
