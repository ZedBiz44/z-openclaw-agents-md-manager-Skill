---
name: z-openclaw-agents-md-manager
description: Audit, create, restructure, shorten, test, or deploy AGENTS.md files for OpenClaw agents, primarily when an external AI operator manages another agent's file.
---

# Z OpenClaw AGENTS.md Manager

Manage another OpenClaw agent's `AGENTS.md` without losing role-specific instructions, authority boundaries, or working safeguards. Treat GitHub as the technical source of truth, Notion as the operating record, and the live runtime as proof of what is actually loaded.

## Scope and Authority

- Use this skill when an external operator such as Cody, Manus, or an approved technical agent is asked to audit, create, reorganize, shorten, repair, test, or deploy another OpenClaw agent's `AGENTS.md`.
- This skill is designed for external management of another OpenClaw agent's `AGENTS.md`. Self-management is outside this skill's intended workflow, but the skill does not create a blanket prohibition or override authority granted elsewhere.
- A request to review or diagnose authorizes read-only inspection only.
- A request to create or optimize authorizes a candidate file and report, not a live deployment unless the user also requests deployment.
- Require confirmation immediately before a production write, restart, configuration change, hook change, permission change, or fleet-wide rollout.
- Never change `bootstrapMaxChars` merely to make an oversized file fit. Fix the information architecture first and present any limit change as a separate decision.

## Choose the Work Mode

- **Audit:** Inspect and report. Do not edit GitHub, Notion, or the live workspace.
- **Candidate:** Create a preservation register, proposed file, diff, and validation report. Commit only when the user asked for repository work.
- **Deploy:** Back up, deploy one approved agent, verify a fresh session, and report. Expand only after the pilot passes and the user approved the broader scope.
- **Create:** Build a new agent file from verified role, authority, routing, runtime, and source-of-truth information. Do not fill gaps with a generic template.

## Required Preflight

Before drafting or changing content:

- Confirm the external operator, target agent, requested mode, servers, repository, branch, and allowed output locations.
- Inspect the live `AGENTS.md`, its path, owner, mode, hash, byte count, character count, line count, and final non-empty lines.
- Inspect repository history and the approved GitHub version. Report drift between GitHub and live state.
- Check the installed OpenClaw version, resolved workspace, `bootstrapMaxChars`, `bootstrapTotalMaxChars`, enabled bootstrap hooks, harness, and recognized bootstrap files.
- Inspect `SOUL.md`, `IDENTITY.md`, `USER.md`, `MEMORY.md`, workspace skills, standing orders, automations, and any legacy `TOOLS.md` or `HEARTBEAT.md` only as needed to decide where instructions belong.
- Use current official OpenClaw documentation for version-sensitive behavior. Do not assume a file is loaded because it exists.
- Inspect `/context detail` or equivalent fresh-session context evidence when available. Do not expose private memory or secrets while doing so.
- Run `scripts/analyze_agents_md.py` against the live file or a protected local copy.
- Read [the AGENTS.md operating standard](references/agents-md-standard.md) before classifying or drafting instructions.
- Read [the audit and deployment procedure](references/audit-and-deployment.md) before any live write.
- Apply [the ZedBiz implementation profile](references/implementation-profile.md) for sources of truth, approval, and records.

## Preserve Instructions Before Editing

- Create an instruction-preservation register from [the register template](assets/instruction-preservation-register.md).
- Record every material instruction or rule group and classify it as:
  - `Retain` - remains substantially intact.
  - `Compress` - shorter wording with the same authority and behavior.
  - `Merge` - combined with an equivalent rule without losing meaning.
  - `Relocate` - moved to the correct loaded file, skill, automation, or technical record.
  - `Retire` - removed only with a documented reason and evidence that it is obsolete, duplicated, unsafe, or superseded.
- Preserve names, ownership, authority limits, approval gates, security restrictions, source-of-truth routing, communication rules, tool constraints, memory privacy, standing orders, and role-specific failure lessons.
- Treat rules added after a previous cleanup as intentional until evidence proves otherwise.
- Never use character reduction as the only reason to delete a rule.
- Do not remove relocated material from `AGENTS.md` until its destination exists, a short routing instruction remains in `AGENTS.md`, and a fresh-session test proves the agent can discover and use the destination.

## Draft the Candidate

- Put high-risk, high-frequency, and identity-defining rules early enough to survive truncation and receive attention.
- Keep role-specific ownership and non-goals clear before shared operating detail.
- Remove repetition, chat-history language, completed incident status, stale paths, and procedural detail that belongs in a skill or automation.
- Keep local tool conventions in the location recognized by the installed OpenClaw version. Current releases use the `## Tools` section in `AGENTS.md`; older or customized fleets must be verified before migration.
- Keep automation authority and approval boundaries in `AGENTS.md`; place schedules in OpenClaw automations. Do not assume a referenced file is auto-injected.
- Keep only the compact standing-order contract in always-loaded context. Move long execution procedures into skills when they can be loaded on demand.
- Keep the candidate between 10,000 and 14,000 OpenClaw characters when practical.
- Treat more than 14,000 characters as a review warning, not automatic failure.
- Block deployment above the target agent's live per-file injection limit.
- If essential content requires 14,001 characters or more, document the reason and prove the tail is loaded in a fresh session.

## Review the Candidate

- Run the analyzer and confirm encoding, size, duplicate headings, and tail text.
- Compare every register entry against the candidate. No item may remain unclassified.
- Check for conflicting authority, duplicated sources of truth, broad permission, invented capabilities, secret material, stale runtime facts, and instructions that belong in another layer.
- Produce a report using [the assessment template](assets/assessment-report.md).
- Show the exact before-and-after byte count, OpenClaw character count, line count, hash, retained safeguards, relocated content, retired content, remaining exceptions, and expected behavior changes.
- Commit the exact candidate and register to the designated GitHub repository before production deployment.

## Deploy and Verify

- Follow [the audit and deployment procedure](references/audit-and-deployment.md).
- Make an external timestamped backup before writing the live file.
- Verify the baseline hash immediately before deployment. Stop if the file changed after the candidate was built.
- Preserve or restore the required owner and file mode.
- Deploy to one approved pilot agent only.
- Start a genuinely fresh session. A successful file copy is not proof that the file was injected.
- Test at least:
  - Role and ownership behavior.
  - One approval or stop boundary.
  - One source-of-truth or routing decision.
  - One agent-specific safeguard.
  - A rule from the final section of the file.
  - A negative case the agent must refuse or route elsewhere.
- Verify the live hash, health, restart count, context evidence, and absence of unintended writes.
- Roll back to the external backup if injection, behavior, health, permissions, or critical-rule tests fail.
- Do not scale until the pilot passes and the user approves the next targets.

## Completion Record

- Record the commit or pull request, candidate and live hashes, counts, backup path, pilot target, validation results, rollback status, and unresolved risks.
- Update the approved Notion SOP or assessment with a link to the GitHub source. Do not paste a competing technical copy into Notion.
- Use plain language: state what changed, what was preserved, what was tested, what remains, and whether it affects operations.
- Finish only when the tested live file matches the committed candidate or the remaining mismatch is clearly reported.

## Failure and Stop Rules

- Stop after three failed attempts at the same check or deployment step.
- Stop when the live file, repository version, runtime configuration, target identity, approval, backup, or rollback path cannot be confirmed.
- Stop if secret values appear in any candidate, diff, log, or report.
- Stop if a new material risk or scope change appears. Return to diagnose, propose the solution, obtain confirmation, and then act.
