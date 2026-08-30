---
name: vercel-deployment
description: Prepare, deploy, verify, and document SaaS web workloads on Vercel using preview-first release practices. Use for Vercel project linking, environment configuration, domains, or production releases.
---

# Vercel Deployment

## Objective

Deploy the correct web component to Vercel with reproducible build settings, safe environment scope, preview evidence, production approval, and rollback context.

## Workflow

1. Discover workspace roots, framework, package manager, build output, Node runtime, and existing Vercel configuration.
2. Verify current CLI commands and platform behavior using official Vercel documentation or installed CLI help.
3. Identify the existing Vercel project before creating a new one; avoid duplicate projects.
4. Define Development, Preview, and Production variable names and consumers without printing values.
5. Run the repository's tests, type checks, and production build.
6. Create or inspect a Preview deployment and smoke-test critical public and authenticated entry points appropriate to the change.
7. Request explicit approval before Production deployment, custom-domain mutation, or secret mutation.
8. Verify the production domain, health, redirects, OAuth callbacks, and deployment status.
9. Record the immutable deployment URL or identifier and rollback method.

## Safety

- Do not assume the repository root is the web root in a monorepo.
- Do not copy production secrets into Preview by default.
- Do not declare success from a successful build alone.
- Preserve current custom domains and project settings unless the task requires change.

Apply `../../core/policies/approval-gates.md`, `../../core/policies/secret-management.md`, `../../core/workflows/provider-integration.md`, and `../../core/workflows/release-lifecycle.md`.
