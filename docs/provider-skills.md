# Provider Skills

Provider skills implement bounded integration workflows. They do not decide product scope or replace platform, data, security, or application ownership.

## Initial Pack

- `environment-contract-manager`
- `supabase-project-setup`
- `vercel-deployment`
- `railway-deployment`
- `openai-integration`

## Provider Documentation

Provider interfaces, pricing, limits, CLI commands, and dashboard navigation change over time. A provider skill should consult current official documentation or installed CLI help when exact behavior matters. Repository references should contain durable decisions and invariants, not copied provider manuals.

## Mutation Policy

Repository preparation may proceed after the task is clear. External project creation, production deployment, domain changes, secret operations, and paid-resource changes require explicit human approval immediately before mutation.
