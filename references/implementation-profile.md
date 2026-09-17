# ZedBiz Implementation Profile

## Identity and Ownership

- Organization and owner: ZedBiz.
- Skill identifier: `z-openclaw-agents-md-manager`.
- Technical source: `https://github.com/ZedBiz44/z-openclaw-agents-md-manager-Skill`.
- License policy: Internal ZedBiz operating skill unless the repository owner publishes a separate licence.
- This skill manages other OpenClaw agents. It never grants self-editing authority to the target agent.

## Platforms and Users

- Initial platform: Codex Desktop, used by Cody.
- Other approved external operators may include Manus and, after separate approval and testing, Victor.
- Victor must not use the skill to edit his own `AGENTS.md`.
- OpenClaw is the managed target platform, not the initial skill runtime.

## Sources of Truth

- GitHub: technical files, candidate files, registers, scripts, diffs, commits, pull requests, and deployment records.
- Live OpenClaw runtime: actual version, configuration, paths, file state, injection behavior, health, and test results.
- Notion `z-Skills`: human SOP and operating guidance linked to GitHub.
- Technical Documentation journal: dated implementation and rollout record when required.

## Operating Controls

- Use Diagnose mode for read-only review: Diagnose, Solution, Confirmation, Act.
- Use Get-er-Done mode for approved creation and bounded implementation.
- A live production write always requires explicit approval even when the skill is automatically discovered.
- Test one agent first, verify it, then request approval before scaling.
- Stop after three failed attempts at the same step.
- Preserve a timestamped external backup and a tested rollback route.

## Security

- Use approved SSH routes and secret-management processes without copying secrets into the skill, repository, logs, prompts, or Notion.
- Never print complete OpenClaw configuration, environment files, private memory, credentials, tokens, or keys.
- Never use broad recursive deletes, ownership changes, or permission changes.
- Never alter bootstrap limits, hooks, services, or runtime configuration as an incidental part of shortening a file.

## Completion Evidence

- Structural and script validation passes.
- GitHub commit identifies the exact tested skill.
- Installed Codex copy matches the committed source.
- Positive, paraphrased, boundary, and negative trigger tests pass.
- Notion SOP links to the GitHub source and states the approval and rollback rules.

