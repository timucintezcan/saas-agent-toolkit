# Getting Started

## Prerequisites

- Codex with `codex plugin` support
- Git access to this public repository
- A target SaaS repository for evaluation or implementation

The target repository does not need to use SaaS Foundation. The toolkit discovers the repository before selecting frameworks, providers, commands, or paths.

## Install a Tagged Release

Pin installation to a release tag for reproducible behavior:

```bash
codex plugin marketplace add timucintezcan/saas-agent-toolkit --ref v0.1.0
codex plugin add saas-agent-toolkit@saas-agent-toolkit
```

Start a new Codex task after installation. Plugin skills are loaded when a task starts.

## Verify the Installation

```bash
codex plugin list
```

Expected state for `v0.1.0`:

- marketplace: `saas-agent-toolkit`;
- plugin: `saas-agent-toolkit@saas-agent-toolkit`;
- status: installed and enabled;
- version: `0.1.0`;
- contents: 8 specialist profiles and 17 skills.

## Make a First Request

Start with an outcome and constraints rather than naming every internal skill:

> Review this repository for release readiness. Run safe local checks, do not deploy, and report missing evidence as NO-GO criteria.

Other useful starting requests:

> Define this project's environment-variable contract without reading or printing secret values.

> Review the Supabase schema, migrations, RLS, and storage policies. Keep the review read-only.

> Prepare a preview-first Vercel deployment plan and stop before production deployment.

> Coordinate this cross-cutting feature across product, application, data, and release concerns.

See [Usage Patterns](usage-patterns.md) for complete workflows.

## Install from a Local Clone

For toolkit development:

```bash
git clone https://github.com/timucintezcan/saas-agent-toolkit.git
codex plugin marketplace add /absolute/path/to/saas-agent-toolkit
codex plugin add saas-agent-toolkit@saas-agent-toolkit
```

After changing the plugin, refresh its marketplace snapshot or reinstall it according to the active Codex CLI behavior. Always verify the installed version and start a new task before testing changed skills.

## Upgrade to a New Tagged Release

Replace `vNEXT` with the target release:

```bash
codex plugin remove saas-agent-toolkit@saas-agent-toolkit
codex plugin marketplace remove saas-agent-toolkit
codex plugin marketplace add timucintezcan/saas-agent-toolkit --ref vNEXT
codex plugin add saas-agent-toolkit@saas-agent-toolkit
```

Then start a new Codex task and run `codex plugin list`.

## Remove the Toolkit

```bash
codex plugin remove saas-agent-toolkit@saas-agent-toolkit
codex plugin marketplace remove saas-agent-toolkit
```

Removing the plugin does not change any target SaaS repository.

## Troubleshooting

### The skills do not appear

Start a new Codex task. Existing tasks may retain the skill set loaded at their creation boundary.

### The wrong version appears

Check `codex plugin list`. Remove the plugin and marketplace, then reinstall using the intended release tag.

### A role skill cannot find shared files

Install the complete plugin. Do not copy individual directories from `skills/`; role adapters reference shared contracts in `agents/` and `core/`.

### A production operation stops for approval

This is expected. Deployment, migration, DNS, secret, destructive-data, and paid-resource mutations require explicit approval immediately before execution.
