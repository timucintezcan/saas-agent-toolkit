---
name: stripe-billing-integration
description: Integrate and verify Stripe payments, subscriptions, webhooks, customer portal, entitlements, and reconciliation for SaaS billing. Use for new Stripe setup or material billing changes.
---

# Stripe Billing Integration

## Objective

Implement test-mode-first SaaS billing that keeps payment data inside Stripe, derives access from verified server-side events, and remains correct across retries, delays, disputes, cancellations, and reconciliation.

## Scope

This skill covers ordinary first-party SaaS payments and subscriptions. Stripe Connect, marketplace fund flows, Treasury, Issuing, lending, and other regulated financial products require separate architecture, legal, risk, and compliance scope.

## Workflow

1. Define the billing model, payer, products, prices, currency, billing interval, trial, tax responsibility, invoice behavior, cancellation, refund, dispute, grace-period, and entitlement rules before implementation.
2. Discover the current payment provider, Stripe account and mode, existing products and prices, customer mapping, database model, authentication, webhook endpoint, background jobs, environments, and financial reporting ownership.
3. Verify current Stripe APIs, SDKs, webhook behavior, test tools, limits, and recommended integration path using official Stripe documentation or installed CLI help.
4. Define sources of truth explicitly. Stripe owns financial state; the application stores provider identifiers, processed-event history, and the minimum derived entitlement state required for product access.
5. Keep secret keys and webhook signing secrets server-only. Expose only provider values designed for the client, and document environment-variable names and ownership without printing values.
6. Isolate Stripe calls behind a billing adapter. Create Checkout, portal, refund, or subscription operations on the server from authenticated user and server-owned product data.
7. Use idempotency for retryable write operations. Persist and process webhook event identifiers idempotently, tolerate duplicate and out-of-order delivery, and make reconciliation safe to rerun.
8. Verify webhook signatures from the unmodified request body using the provider's current mechanism. Do not grant paid access from client redirects, query parameters, or unverified events.
9. Model relevant lifecycle states, including incomplete or failed payment, active, trialing, past due, paused when applicable, canceled, refunded, and disputed. Define which states grant, retain, restrict, or revoke access.
10. Keep product and price identifiers stable and environment-specific. Do not infer price, currency, discount, or entitlement from client input.
11. Configure customer self-service only for approved actions. Validate return destinations and ensure portal changes follow the same webhook and entitlement path.
12. Request explicit approval before creating or changing live products, prices, coupons, tax settings, webhook endpoints, API keys, portal configuration, production entitlements, or any operation that can create a real charge, refund, payout, or billing obligation.
13. In test mode, verify successful and failed payment, required authentication, duplicate and delayed webhook delivery, subscription upgrade or downgrade when supported, cancellation, refund, dispute simulation when available, and reconciliation after missed events.
14. Before live enablement, document support ownership, refund and dispute handling, financial reconciliation, monitoring, disable path, and rollback limits.

## Safety

- Never request, log, store, or process raw card or bank credentials outside Stripe-hosted or Stripe-approved collection surfaces.
- Never expose secret keys or webhook signing secrets to browser or mobile bundles.
- Do not create live charges or mutate production billing because test mode succeeded.
- Do not trust client success callbacks as payment confirmation.
- Do not delete or recreate live financial resources merely to simplify configuration.
- Keep billing logs free of sensitive payment data and unnecessary personal information.
- Treat dashboard access as inspection and preparation authority only; live final actions follow the shared UI-assisted approval contract.

## Output

Report the billing and entitlement model, provider-resource ownership, environment and secret-name contract, webhook and idempotency design, test-mode evidence, lifecycle coverage, reconciliation method, live approval gates, operational ownership, and rollback or disable instructions.

Apply `../../core/policies/approval-gates.md`, `../../core/policies/secret-management.md`, `../../core/workflows/provider-integration.md`, and `../../core/workflows/release-lifecycle.md`.
