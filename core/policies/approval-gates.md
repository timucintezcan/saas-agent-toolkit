# Approval Gates

## Principle

Authorization to plan or prepare a workflow is not authorization to mutate production systems.

## Explicit Approval Required

Request human approval immediately before:

- deploying to a production environment;
- applying a production database migration, backfill, or restore;
- deleting or irreversibly transforming user or production data;
- changing RLS, IAM, authentication, or tenant-isolation policies;
- changing DNS, domains, TLS, or OAuth callback configuration;
- creating, rotating, revoking, or exposing a secret;
- enabling a new paid service, model, scheduled task, or billing plan;
- disabling a security control, alert, backup, or monitoring rule.

## Safe Without Mutation Approval

- repository discovery;
- read-only provider inspection;
- local validation;
- static analysis;
- generating a plan, migration file, runbook, or preview configuration;
- running non-destructive tests in an isolated local environment.

## Approval Request

State the exact target, expected mutation, user-visible impact, rollback path, and verification step. Do not bundle unrelated high-risk actions into one approval.

## Interactive UI Boundary

An authenticated provider session allows inspection and authorized preparation; it does not authorize mutation by itself.

When a UI operation reaches a final control such as Save, Deploy, Create, Delete, Rotate, Revoke, Transfer, Purchase, Enable, or Send, request approval immediately before activating that control when the resulting operation is covered by an approval gate.

After approval, activate only the described control for the confirmed account, project, resource, and environment. A prior approval to plan, navigate, populate fields, or create a preview does not carry forward to a later production action.
