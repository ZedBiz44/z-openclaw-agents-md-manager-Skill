# Audit and Deployment Procedure

Read this reference before changing a live OpenClaw agent.

## Read-Only Audit

- Resolve the server, runtime type, login route, container or service, workspace path, and target identity.
- Read the live file through the active runtime when host permissions or mounts can hide it.
- Capture the live SHA-256 hash, owner, mode, bytes, OpenClaw characters, lines, and tail.
- Capture `openclaw --version` from the target runtime.
- Read only the relevant configuration keys: workspace, harness, bootstrap limits, hooks, and agent overrides. Never print complete configuration or environment files.
- List recognized bootstrap files and note legacy files without modifying them.
- Capture the GitHub version and history. Explain live-to-repository drift.
- Inspect fresh-session context detail when available, redacting private information.

## Candidate Workflow

- Copy the live file into a protected work area.
- Create the instruction-preservation register before editing.
- Draft the candidate from verified live, GitHub, role, and runtime evidence.
- Run `scripts/analyze_agents_md.py` on both versions.
- Review the diff line by line against the register.
- Commit the candidate, register, and assessment to a branch or pull request.
- Record the exact candidate hash that is approved for deployment.

## Production Gate

Immediately before a live write:

- Confirm the user approved deployment and the exact pilot agent.
- Re-read the live hash. Stop if it differs from the audited baseline.
- Create a timestamped external backup outside the live workspace file.
- Confirm the rollback command or copy method can restore that backup.
- Confirm the required owner and mode.
- Confirm no unrelated configuration, hook, service, agent, or file is included.

## Deployment

- Use the target's established safe write route.
- Do not use broad recursive ownership or permission changes.
- Write only the approved candidate.
- Restore or confirm the expected owner and mode.
- Re-read the live hash and compare it with the approved candidate.
- Avoid restarting the Gateway when a fresh session is sufficient. Restart only when the installed runtime or changed configuration requires it.

## Fresh-Session Verification

- Start a new session that cannot reuse cached bootstrap content.
- Inspect context detail where supported.
- Ask behavior questions rather than requesting exact quotation.
- Test the agent's role, non-goal, approval gate, routing rule, unique safeguard, and final-section rule.
- Use a safe negative test that requires refusal, escalation, or handoff.
- Confirm the agent remains healthy and did not perform unintended writes or external actions.

Do not claim `truncated=false` unless the runtime reports it. When native injection metadata is unavailable, describe tail-rule behavior as practical evidence, not proof of the complete injected text.

## Rollback

Roll back when:

- The live hash does not match the approved candidate.
- Ownership or permissions are wrong.
- The runtime becomes unhealthy or restarts unexpectedly.
- A critical rule is missing, misunderstood, or truncated.
- The agent performs or claims authority it should not have.
- The deployment changed an unapproved file or system.

Restore the external backup, restore owner and mode, start another fresh session, and verify the last known-good behavior. Record the failure and stop before attempting a broader rollout.

## Completion Proof

Save:

- Target and runtime version.
- Baseline, candidate, deployed, and backup hashes.
- Before-and-after counts.
- Preservation register.
- GitHub commit or pull request.
- Backup location.
- Fresh-session prompts and observed results.
- Health and restart evidence.
- Rollback result or confirmation that rollback was not needed.
- Remaining exceptions and next approved target.

