# ZedBiz OpenClaw AGENTS.md Operating Standard

Use this reference when assessing instruction placement, order, size, duplication, or completeness.

## Primary Job

`AGENTS.md` is the always-loaded operating contract for an OpenClaw agent. It should tell the agent what it owns, what it must not do, how it makes decisions, when approval is required, where work belongs, and how it hands work off.

Do not turn it into a complete company handbook, tool manual, incident archive, or personality file.

## Recommended Order

Use this order unless the target agent has a verified reason to differ:

- Purpose and operating contract.
- Agent setup, authority, reporting line, and source-of-truth summary.
- Role summary, owned work, non-goals, and role-specific rules.
- Operating modes, including Get-er-Done and Diagnose when applicable.
- Approval gates, safety boundaries, security, and external-action limits.
- Routing, handoffs, lane ownership, and delegation limits.
- Memory, knowledge lookup, privacy, and durable-record rules.
- Tool and local-environment conventions recognized by the installed runtime.
- Communication and channel-formatting rules that genuinely apply.
- Compact standing-order contracts and automation boundaries.
- Completion, verification, maintenance, and escalation rules.

Safety and authority rules belong near the beginning when they govern most work. Important tail rules must still be tested because runtime truncation can remove them.

## What Belongs in Each Layer

### AGENTS.md

- Durable operating rules and priorities.
- Role ownership and non-goals.
- Approval and stop boundaries.
- Source-of-truth routing and handoffs.
- Memory-use and privacy rules.
- Local tool conventions required in normal work.
- Compact standing-order authority, trigger, approval, escalation, and prohibited-action rules.
- Specialist-lane contract when the agent participates in multi-agent routing.
- Instructions that Codex subagents must inherit.

### SOUL.md

- Persona, voice, tone, temperament, and conversational style.
- Do not duplicate operating authority here.

### IDENTITY.md

- Agent name, identity, vibe, and stable identifying details.

### USER.md

- Stable user preferences, communication directives, relationships, and active-project context.
- Respect the runtime's separate `USER.md` character limit.

### MEMORY.md and daily memory

- Durable facts, decisions, lessons, and session continuity.
- Never use memory as the sole source for current technical truth.
- Load private long-term memory only in approved private/main contexts.

### Skills

- Detailed repeatable procedures.
- Tool-specific methods.
- Long checklists, examples, schemas, and conditional workflows.
- Validation and rollback procedures that are needed only for a matching task.

### Automations and hooks

- Schedules, event triggers, repeat timing, and lifecycle execution.
- Keep authority and safety limits in `AGENTS.md`; keep timing and runtime enforcement in the automation or hook.

### GitHub and Notion

- GitHub holds the authoritative technical file, history, scripts, and deployment records.
- Notion holds the human SOP, operating explanation, approvals, and summaries, linked to GitHub.

## Version-Sensitive Files

- Current OpenClaw documentation places local tool notes in `AGENTS.md` under `## Tools` and does not recognize root `TOOLS.md` as a bootstrap file.
- Current OpenClaw documentation treats the old workspace `HEARTBEAT.md` pattern as retired; proactive work is controlled through current automation and heartbeat mechanisms.
- Older or customized deployments may still contain either file. Inspect the installed version, Doctor findings, hooks, and actual injected context before moving or deleting content.
- `BOOT.md` runs only when the relevant startup hook is enabled. Existence alone does not make it active.
- Arbitrary referenced files are not guaranteed to be injected. Verify bootstrap hook allowlists and `/context detail`.

## Retired TOOLS.md Cleanup

- Verify the installed runtime and resolved workspace first. Current OpenClaw uses `AGENTS.md` → `## Tools`; do not recreate `TOOLS.md` just because an old instruction or old session tries to read it.
- If the legacy file exists, back it up outside the active workspace, account for every customized note, and verify the merged destination before removing the active original. Preserve owner, mode, and reader access. The official migration uses `openclaw doctor --fix`; do not run broad Doctor repairs solely for this cleanup without reviewing their other effects and authority.
- If migration already happened, preserve the existing Tools content and archive. Correct the remaining instructions instead of reimporting notes, deleting recovery copies, or creating a compatibility file.
- Search active `AGENTS.md`, `SOUL.md`, `IDENTITY.md`, other loaded core files, applicable skills, and scripts for instructions to read, write, or recreate `TOOLS.md`. Inspect hooks and active workspace paths; do not blindly replace historical source labels, migration headings, backups, archived transcripts, or unrelated platforms' instructions.
- OpenClaw's automatic rewrite can match only standard phrases. Customized wording can survive even when the file was successfully migrated. Replace each obsolete instruction with the actual `Tools` section of `AGENTS.md`, retaining the original task conditions, privacy restrictions, identity checks, and approval boundaries.
- Check the merged file against the live per-file and total context limits. Do not increase limits or discard rules as an incidental cleanup. Preserve unrelated file content and compare baseline hashes immediately before writing.
- Test one agent first in a genuinely fresh session: it must locate its current tool notes, retain a role-specific safeguard, and handle a missing legacy file without recreating it. Verify a final-section rule as behavioral evidence; `native_unverified` context metadata alone does not certify complete injection. Then expand only within the user's approved scope.
- Record exact changed files, preserved notes, hashes, backup paths, fresh-session results, and any remaining active references. Older conversations may retain obsolete instructions; distinguish those from current files.

Official reference: [TOOLS.md retired](https://docs.openclaw.ai/reference/templates/TOOLS).

## Size Standard

- Target: 10,000 to 14,000 OpenClaw characters.
- Warning: more than 14,000 characters.
- Hard stop: the live `bootstrapMaxChars` limit for the target agent.
- Default OpenClaw values may be 20,000 characters per file and 60,000 total, but live configuration wins.
- Count OpenClaw characters as UTF-16 code units, not UTF-8 bytes.
- Do not raise limits to hide poor instruction design.
- A justified file above 14,000 characters requires a documented exception and fresh-session tail verification.

## Quality Tests

The finished file must be:

- Complete enough that the agent can work without guessing its authority.
- Short enough that critical instructions are loaded.
- Specific to the target role.
- Free from duplicate or conflicting rules.
- Free from secrets and unsupported capability claims.
- Clear about external actions and approvals.
- Clear about what the agent does not own.
- Aligned with the live runtime, not only a historical template.

## Current Official References

Check these pages again during version-sensitive work:

- [AGENTS.md template](https://docs.openclaw.ai/reference/templates/AGENTS)
- [Default AGENTS.md](https://docs.openclaw.ai/reference/AGENTS.default)
- [Agent workspace](https://docs.openclaw.ai/concepts/agent-workspace)
- [Codex workspace bootstrap files](https://docs.openclaw.ai/plugins/codex-harness-reference/workspace-bootstrap-files)
- [Standing orders](https://docs.openclaw.ai/automation/standing-orders)
- [Parallel specialist lanes](https://docs.openclaw.ai/concepts/parallel-specialist-lanes)
- [Bundled hooks](https://docs.openclaw.ai/automation/hooks/bundled-hooks)
