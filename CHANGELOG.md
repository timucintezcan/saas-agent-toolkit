# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.3.0] - 2026-08-31

### Added

- Hybrid mobile delivery skill for keeping one mobile-first web UI aligned across browser, PWA, iOS, and Android through Capacitor.
- Hybrid SaaS guidance in the Bootstrap Advisor, including the distinction between Capacitor packaging and a separate Expo application.
- Candidate roadmap entries for GitHub CI/CD delivery, Playwright end-to-end browser quality, and SaaS security review workflows.

### Changed

- Updated Codex and Claude Code installation guidance, plugin manifests, and release metadata for version `0.3.0`.
- Clarified the agent model, architecture, onboarding, and skill catalog for the current twenty-two-skill toolkit.

## [0.2.0] - 2026-08-31

### Added

- Initial Claude Code plugin-directory adapter with shared namespaced skills and adapter boundary documentation.
- Native Claude Code metadata for all eight specialist agent profiles.
- Cloudflare domain and edge operations skill with DNS, TLS, proxy, redirect, cache, and rollback controls.
- Sentry observability setup skill with release, source-map, privacy, sampling, alert, and controlled-event verification.
- Resend transactional email integration skill with domain authentication, idempotency, webhook, retry, and delivery controls.
- Deterministic validation that keeps the public skill catalog aligned with installed skill directories.
- Shared UI-assisted provider execution mode with authenticated-session, credential-handoff, prompt-injection, final-action approval, and evidence rules.
- Stripe billing integration skill with test-mode-first payments, subscriptions, verified webhooks, idempotency, entitlements, portal, and reconciliation controls.

## [0.1.1] - 2026-08-31

### Added

- Local Codex installation and discovery verification against a real SaaS repository.
- Git and local-path Codex marketplace packaging.
- Installation, usage, and release documentation.
- Complete skill catalog, usage patterns, and upgrade guidance.

### Changed

- Reworked the README as a public agent-toolkit entry point with explicit scope, routing, safety, architecture, and documentation navigation.
- Expanded agent-model, architecture, and contribution contracts for maintainers and adapter authors.

## [0.1.0] - 2026-08-30

### Added

- Eight product-agnostic specialist agent profiles.
- Seventeen Codex skills covering orchestration, application, data, platform, quality, observability, environment contracts, Supabase, Vercel, Railway, OpenAI, scaffolding, deployment profiles, and release readiness.
- Vendor-neutral roles, policies, task contracts, provider workflows, and release workflows.
- Repository, skill, and plugin validation with GitHub Actions.
- MIT license, contribution guidance, and security policy.

[Unreleased]: https://github.com/timucintezcan/saas-agent-toolkit/compare/v0.3.0...HEAD
[0.3.0]: https://github.com/timucintezcan/saas-agent-toolkit/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/timucintezcan/saas-agent-toolkit/compare/v0.1.1...v0.2.0
[0.1.1]: https://github.com/timucintezcan/saas-agent-toolkit/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/timucintezcan/saas-agent-toolkit/releases/tag/v0.1.0
