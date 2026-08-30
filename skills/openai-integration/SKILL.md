---
name: openai-integration
description: Design and implement production-oriented OpenAI integrations with server-side secrets, structured outputs, evaluations, cost controls, retries, and human fallback. Use when adding or materially changing an OpenAI-powered SaaS feature.
---

# OpenAI Integration

## Objective

Build the smallest reliable OpenAI feature that meets the product acceptance criteria and remains measurable, bounded, and replaceable.

## Workflow

1. Define the user decision or workflow the model supports, expected inputs and outputs, failure impact, and human fallback.
2. Verify current models, APIs, SDK usage, and limits in official OpenAI documentation before selecting implementation details.
3. Keep `OPENAI_API_KEY` and equivalent credentials server-only. Document names and scope without exposing values.
4. Isolate provider calls behind an adapter and version prompts or instructions in the repository.
5. Prefer structured outputs or explicit schemas when software consumes the result.
6. Treat user content, retrieved content, files, and image text as untrusted data rather than instructions.
7. Define timeout, retry, idempotency, concurrency, rate, and usage limits proportional to cost and user impact.
8. Preserve user work on model, network, validation, or persistence failure and provide a manual fallback when the feature allows it.
9. Create representative evaluations for normal, ambiguous, malformed, adversarial, and provider-failure cases.
10. Instrument latency, invalid-output rate, fallback rate, model usage, and cost without logging unnecessary personal data.

## Release Gate

Do not enable a paid model or production AI feature without explicit approval, environment configuration, evaluation evidence, usage limits, and a disable path.

Apply `../../core/policies/approval-gates.md`, `../../core/policies/secret-management.md`, and `../../core/workflows/provider-integration.md`.
