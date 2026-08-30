# Release Lifecycle

## 1. Discover

Identify repository instructions, environments, deployment topology, migrations, secrets by name, and existing release automation.

## 2. Validate Locally

Run the narrowest relevant checks first, then the repository's release verification commands. Do not fix unrelated failures.

## 3. Prepare Preview

Build a preview or dry-run configuration when the provider supports it. Verify environment-variable names without exposing values.

## 4. Smoke Test

Test health, authentication entry points, critical routes, and provider integrations appropriate to the change.

## 5. Request Production Approval

Summarize the exact mutation, risk, expected impact, rollback path, and evidence from validation.

## 6. Release

Apply approved migrations in the documented order, deploy the application, and record immutable deployment references.

## 7. Verify and Observe

Repeat production smoke tests and inspect errors, latency, background jobs, and cost signals. Roll back or stop when acceptance criteria fail.
