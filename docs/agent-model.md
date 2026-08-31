# Agent Model

## Definitions

- **Agent profile:** Vendor-neutral outcome ownership, decision boundary, and output contract stored in `agents/`.
- **Role:** Durable engineering responsibility stored in `core/roles/`.
- **Skill:** A bounded, discoverable procedure or role adapter exposed by an agent platform.
- **Adapter:** Packaging that makes profiles and skills usable in a specific coding agent.
- **Tool:** A deterministic execution primitive such as a CLI, API, script, browser, or MCP server.

## Runtime Model

Codex exposes specialist profiles through role skills. Activating a role skill makes the current Codex agent adopt that outcome contract and select narrower workflow or provider skills as needed.

Claude Code loads the same `SKILL.md` procedures as namespaced skills and the specialist profiles in `agents/` as namespaced subagents. The profile body remains the shared outcome contract; Claude-specific frontmatter only provides the metadata required for native loading.

This is coordinated role execution, not a claim that every profile runs as an independent parallel process. True parallel multi-agent execution requires a supporting runtime, isolated work ownership, conflict handling, and integrated verification.

## Source of Truth

```text
core roles, workflows, and policies
                ↓
vendor-neutral agent profiles
                ↓
Codex role skills and Claude Code subagents
                ↓
focused workflow and provider skills
                ↓
deterministic tools and verification evidence
```

Adapter files remain thin. Shared rules belong in `core/`; outcome ownership belongs in `agents/`; provider mechanics belong in focused skills.

## Routing Model

Use the smallest ownership surface that can complete the objective:

1. **Narrow procedure skill** when one bounded workflow owns the result.
2. **Specialist role skill** when several related judgments belong to one discipline.
3. **Delivery Orchestrator** when dependencies cross specialist boundaries.

The orchestrator may route and integrate work, but it does not absorb specialist responsibilities or authorize production mutation.

## Execution Lifecycle

Every non-trivial execution follows this lifecycle:

1. **Contract:** establish objective, scope, constraints, acceptance evidence, and approval gates.
2. **Discover:** inspect repository instructions, architecture, provider state, and existing conventions.
3. **Route:** select the smallest suitable specialist and procedure set.
4. **Plan:** order dependencies and separate repository work from external mutation.
5. **Execute:** make focused changes or perform approved operations.
6. **Verify:** collect tests, build results, migration checks, smoke tests, or provider evidence.
7. **Decide:** report completion, risk, or release status without hiding missing evidence.
8. **Handoff:** identify remaining approvals, rollback context, and follow-up ownership.

## Delegation Contract

Delegation must include:

- the exact outcome owned by the specialist;
- inputs and repository scope;
- constraints and forbidden mutations;
- required evidence;
- unresolved decisions that must return to the orchestrator or user.

Production authorization cannot be delegated. A specialist may prepare and validate a production action, but the human approval gate remains external to the agent hierarchy.

## Evidence Contract

An agent output should distinguish:

- **Observed:** directly verified repository or provider state;
- **Changed:** files or external state intentionally modified;
- **Validated:** checks executed and their results;
- **Inferred:** conclusions drawn from evidence but not directly measured;
- **Blocked:** missing permission, data, provider state, or user decision;
- **Deferred:** intentionally excluded scope.

This prevents confident wording from replacing observable completion.

## Failure Behavior

Agents stop or return control when:

- a required production approval is missing;
- a secret value would need to be exposed;
- repository instructions conflict with the requested action;
- critical validation fails;
- provider state is ambiguous and mutation could create duplicates or cost;
- the task requires ownership outside the selected profile.

Stopping safely is a successful application of the model, not an execution failure.
