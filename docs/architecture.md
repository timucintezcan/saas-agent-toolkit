# Architecture

## Objective

SaaS Agent Toolkit separates durable engineering knowledge from agent-platform packaging and provider-specific mechanics.

## Repository Structure

```text
.agents/plugins/marketplace.json   Codex marketplace entry
.codex-plugin/plugin.json          Codex plugin manifest
.claude-plugin/plugin.json         Claude Code plugin manifest
adapters/                          Platform-specific loading guidance
agents/                             Specialist outcome contracts
core/roles/                         Durable discipline ownership
core/workflows/                     Shared execution contracts
core/policies/                      Safety and portability invariants
skills/                             Codex adapters and bounded procedures
scripts/                            Deterministic repository validation
tests/                              Validator behavior tests
docs/                               User, architecture, and release guidance
```

## Layers

### Core

`core/` is the vendor-neutral source of truth. Core documents describe responsibilities, execution invariants, approval gates, and safety requirements without depending on Codex, Claude Code, a model, or a cloud provider.

### Agent Profiles

`agents/` defines durable outcome ownership, activation boundaries, delegation rules, and output contracts. Profiles are platform-neutral and should change less frequently than adapter skills.

### Skills

`skills/` contains bounded procedures loaded by both Codex and Claude Code. Role skills expose agent profiles in Codex. Workflow and provider skills add focused mechanics while referencing shared core contracts.

### Deterministic Support

`scripts/` and `tests/` enforce structure that should not depend on model interpretation: manifest shape, marketplace packaging, skill metadata, required files, and local documentation links.

### Adapter Support

Codex and Claude Code are supported in `v0.2.0`. Adapters must consume the same core and profile contracts instead of copying them into a second source of truth.

## Dependency Direction

```text
agent-platform adapter ──→ agent profile ──→ core role/workflow/policy
provider skill ──────────→ shared provider workflow and safety policy
validator ───────────────→ repository structure and public contracts
core ────────────────────→ no adapter or provider dependency
```

Dependencies do not point from core into Codex, provider dashboards, SaaS Foundation, or user applications.

## Ownership Boundaries

- Product-specific requirements stay in the target product repository.
- SaaS Foundation generator behavior stays in SaaS Foundation.
- Reusable SaaS delivery contracts belong here.
- Provider-specific mechanics belong in one focused provider skill.
- Secret values and private provider state never belong in this repository.

## Portability Contract

Skills must support:

1. projects generated from SaaS Foundation;
2. existing repositories with different layouts;
3. monorepos and single-application repositories;
4. repositories using only a subset of supported providers;
5. read-only analysis when mutation is not authorized.

Every skill begins with discovery and preserves existing architectural choices unless the user explicitly requests a change.

## Extension Rules

### Add a core contract when

- several profiles or skills need the same invariant;
- the rule is durable across providers and adapters;
- duplication would create safety or consistency drift.

### Add an agent profile when

- the outcome has durable ownership;
- it requires recurring judgment and delegation boundaries;
- no existing specialist can own it cleanly.

### Add a skill when

- the task is bounded and repeated;
- activation can be described narrowly;
- verification and stopping conditions are observable.

### Add a script when

- deterministic automation materially improves safety or reliability;
- the behavior can be tested without provider credentials;
- model reasoning would add unnecessary variability.

## Versioning and Compatibility

- Patch releases correct behavior or documentation without changing public contracts materially.
- Minor releases may add profiles, skills, providers, or backward-compatible contract fields.
- Major releases may change routing, approval, packaging, or adapter contracts incompatibly.
- Release notes must state supported adapters, validation evidence, and known limitations.

SaaS Foundation and target applications remain test targets, not runtime dependencies.
