---
name: resend-email-integration
description: Integrate and verify Resend transactional email, sending domains, templates, webhooks, retries, and delivery controls for SaaS applications. Use for new Resend setup or material email-flow changes.
---

# Resend Email Integration

## Objective

Deliver transactional SaaS email reliably without exposing credentials, duplicating sends, damaging domain authentication, or silently losing delivery failures.

## Scope

This skill covers transactional messages such as authentication, invitations, receipts, and product notifications. Marketing campaigns, audience management, and consent programs require separate product and compliance scope.

## Workflow

1. Define each email's user event, recipient, required content, timing, retry tolerance, duplicate-send impact, localization needs, and manual fallback.
2. Discover the current email provider, sending abstraction, background jobs, templates, environment model, domains, DNS provider, webhook endpoints, and existing Resend account state.
3. Verify current Resend SDK, API, domain-authentication, testing, webhook, and limit behavior using official documentation or installed CLI help.
4. Reuse the appropriate existing domain and provider resources. Keep API keys server-only and document environment-variable names and ownership without exposing values.
5. Prepare SPF and DKIM records while preserving existing mail infrastructure. Coordinate DMARC deliberately and never replace a shared SPF record blindly.
6. Isolate provider calls behind an application adapter. Keep templates versioned, testable, accessible, and safe for untrusted user content.
7. Define deterministic idempotency, retry, timeout, queue, and failure behavior. Preserve user state when email delivery fails and prevent retries from sending duplicates.
8. Verify webhook signatures using the provider's current mechanism, reject stale or invalid events, and process retries idempotently.
9. Separate local, preview, staging, and production recipients and domains. Prevent preview deployments from emailing real users by default.
10. Request explicit approval before domain or DNS mutation, API-key creation or rotation, webhook creation, production sending, real-recipient tests, or paid-resource changes.
11. Test representative rendering and non-production delivery. Verify provider acceptance, domain status, message identity, links, reply behavior, bounce or complaint handling, and webhook processing.

## Safety

- Never expose API keys or webhook secrets to browser or mobile bundles.
- Do not log full message bodies or unnecessary recipient data.
- Do not use transactional authorization to introduce marketing email.
- Do not send test messages to real recipients without explicit approval.
- Do not declare success from an accepted API request alone; verify the required delivery and event path.

## Output

Report supported message flows, domain-authentication state, environment and secret-name contract, idempotency and retry behavior, rendering and delivery evidence, webhook verification, fallback behavior, and rollback or disable instructions.

Apply `../../core/policies/approval-gates.md`, `../../core/policies/secret-management.md`, and `../../core/workflows/provider-integration.md`.
