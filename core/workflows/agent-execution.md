# Agent Execution Contract

## Purpose

An agent owns an outcome across multiple steps. A skill performs a bounded reusable procedure. An agent may select skills, but a skill must not silently expand the user's objective.

## Execution Stages

1. **Discover:** Read repository instructions, architecture, current state, and available validation commands.
2. **Frame:** State the objective, scope, assumptions, dependencies, and approval gates.
3. **Plan:** Break work into verifiable outcomes and identify specialist or skill boundaries.
4. **Execute:** Make the smallest coherent changes while preserving repository conventions.
5. **Verify:** Run focused checks before broader release checks.
6. **Report:** Describe completed outcomes, evidence, unresolved risks, and the next decision.

## Delegation

- Delegate only when another profile has a clearer outcome boundary.
- Provide the delegated task with objective, relevant context, constraints, and expected output.
- Do not delegate approval decisions.
- The originating agent remains responsible for integrating and validating delegated results.

## Completion

An agent may declare completion only when acceptance criteria are met, required checks have run, and unresolved risks are explicit. Missing production authorization is a stop condition, not permission to improvise.
