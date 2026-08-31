---
name: cloudflare-domain-operations
description: Configure and verify Cloudflare zones, DNS, proxy, TLS, redirects, caching, and basic edge security for SaaS domains. Use when onboarding a domain or materially changing Cloudflare traffic controls.
---

# Cloudflare Domain Operations

## Objective

Route SaaS traffic through Cloudflare without breaking application, authentication, email, or provider-verification flows, and leave verifiable rollback context.

## Scope

This skill covers zones, DNS, proxy state, TLS, redirects, caching, basic edge security, and domain verification. Use a dedicated workflow for Workers, Pages application development, R2, D1, Queues, or other application platforms.

## Workflow

1. Discover the registrar, authoritative nameservers, existing zone, DNS records, origin providers, application domains, authentication callbacks, mail records, verification records, DNSSEC, TLS mode, proxy state, redirects, and cache rules.
2. Verify current Cloudflare behavior, API or CLI commands, and provider-specific record requirements using official documentation or installed CLI help.
3. Capture a redacted baseline and desired record-level diff. Identify records controlled by another provider and records that must remain DNS-only.
4. Preserve MX, SPF, DKIM, DMARC, CAA, and ownership-verification behavior. Do not replace an existing SPF policy blindly or proxy protocols that Cloudflare does not support.
5. Prefer end-to-end TLS and explicit redirect behavior. Do not weaken origin validation or security settings to hide an origin problem.
6. Prepare the smallest change set, propagation expectations, verification checks, and rollback values before mutation.
7. Request explicit approval immediately before zone creation, nameserver change, DNS mutation, proxy-state change, TLS-mode change, redirect or cache-rule mutation, edge-security change, DNSSEC change, or email-routing change.
8. Apply only the approved diff and record immutable provider identifiers when available.
9. Verify authoritative DNS, TLS certificate and hostname behavior, HTTP redirects, origin health, cache behavior, critical application paths, authentication callbacks, and email delivery when affected.

## Safety

- Never print API tokens, origin credentials, or secret verification material.
- Avoid duplicate zones and records by discovering account and zone state first.
- Do not delete apparently stale records without ownership evidence and rollback context.
- Treat apex, wildcard, authentication, mail, and provider-verification records as high-impact.
- Do not declare success while DNS propagation, certificate issuance, or origin health remains unverified.

## Output

Report the baseline, approved diff, records preserved, verification evidence, propagation state, rollback instructions, and any remaining registrar or provider dependency.

Apply `../../core/policies/approval-gates.md`, `../../core/policies/secret-management.md`, `../../core/workflows/provider-integration.md`, and `../../core/workflows/release-lifecycle.md`.
