---
name: hybrid-mobile-delivery
description: Prepare a mobile-first web SaaS for PWA and Capacitor-based iOS and Android delivery while preserving one shared UI and product flow. Use when a web product needs store packaging without a separate native application.
---

# Hybrid Mobile Delivery

## Objective

Deliver one mobile-first web product that remains usable in the browser and PWA, and can be packaged for iOS and Android through Capacitor without duplicating product UI or business logic.

## Discovery

Determine:

- whether the product needs browser-only delivery, installable PWA, or store distribution;
- whether its web build can produce static client assets for the mobile shell;
- required device capabilities, such as camera, file access, notifications, deep links, or local storage;
- whether a capability is essential at launch or can be deferred;
- the app identifier owner and store-release timing.

## Operating Rules

- Keep all product screens, navigation, and domain behavior in the web application.
- Implement and validate the `375px` layout first; progressively enhance larger viewports.
- Use Capacitor plugins only behind a small platform adapter. Provide a browser fallback or hide non-essential device actions gracefully.
- Keep primary flows usable in browser and PWA before adding a device-specific enhancement.
- Do not create a second Expo or React Native UI merely to package the same product.
- Do not create iOS or Android platform projects until the app identifier, required platform tooling, and a store-build need are confirmed.
- Route store signing, paid accounts, permission declarations, and production releases through explicit human approval.

## Delivery Sequence

1. Select `hybrid-saas` when a single web UI is the intended product surface.
2. Make the web UI mobile-first and verify the primary flow at `375px`, `768px`, and `1280px`.
3. Add PWA behavior only when offline or installability provides product value.
4. Add the minimum Capacitor plugins for launch-critical device capabilities.
5. Build and sync the web bundle to the Capacitor shell.
6. Create platform projects and configure signing only when a store build is approved.
7. Verify browser, PWA, iOS, and Android behavior with the same acceptance criteria.

## Output

Provide:

1. the selected delivery target and its rationale;
2. a list of shared web capabilities and isolated device adapters;
3. required environment-variable names, permission declarations, and deep-link domains without secret values;
4. responsive, browser, PWA, and platform validation evidence;
5. the next human approval gate before any store, signing, or paid-resource mutation.

Apply `../../core/workflows/task-contract.md` and route deployment changes through `saas-platform-agent`.
