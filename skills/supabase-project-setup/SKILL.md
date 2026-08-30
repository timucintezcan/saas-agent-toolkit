---
name: supabase-project-setup
description: Integrate a SaaS repository with Supabase database, Auth, Storage, migrations, RLS, and generated types. Use for new Supabase setup or material changes to an existing integration.
---

# Supabase Project Setup

## Objective

Create a least-privilege, migration-driven Supabase integration that remains testable locally and safe to release.

## Workflow

1. Discover the framework, current data layer, authentication model, migration history, storage needs, and target environments.
2. Confirm which Supabase capabilities are required; do not enable Auth, Storage, Realtime, Edge Functions, or Cron without a product need.
3. Verify current setup details in official Supabase documentation or installed CLI help.
4. Define public client configuration separately from server-only or service-role credentials.
5. Add ordered migrations, constraints, indexes justified by access paths, RLS policies, and storage policies.
6. Keep user identity server-derived and test tenant or row isolation with negative cases.
7. Generate or update database types when the project uses them.
8. Run local migration, SQL, integration, and application checks before hosted changes.
9. Prepare the hosted migration order, verification queries, and recovery path.

## Safety

- Never expose a service-role key to a browser or mobile bundle.
- Never disable RLS to make an integration work.
- Treat production migrations, policy changes, backfills, Auth provider changes, Storage mutations, and Cron creation as approval-gated operations.
- Do not rerun historical migrations blindly; use the repository's migration state and forward-fix policy.

Apply `../../core/policies/approval-gates.md`, `../../core/policies/secret-management.md`, and `../../core/workflows/provider-integration.md`.
