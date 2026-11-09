# Current development handoff

Reviewed: 2026-11-09 — Middletown MacBook.

## Current state

The approved source/context backup is on https://github.com/leofari/nyt-spelling-bee-helper-project (public). Start from `main`; fetch all remote branches before comparing with another Mac. Initial verified main before this documentation refresh: `69434a9d94be3addaf03ef33218423fa77abb829`. Current commit: inspect `git rev-parse HEAD`.

Find candidate words under Spelling Bee letter constraints.

## Completed in this backup

- Preserved existing history and meaningful alternate versions without force-pushing or deleting branches.
- Added project context, source provenance and an additive AGENTS.md handoff-maintenance instruction.
- Kept Codex transcripts, credentials and private runtime data out of the upload.
- Verified source manifests and remote commit identities; application behavior was not newly regression-tested.

## Alternate versions

- No additional source archive branch was needed.

## Next concrete step

Review existing README and validate against a small known letter set before changes.

## Constraints

Exclude unrelated Downloads data; existing repository is PUBLIC.

Original source working trees were not edited by the backup. Do not assume a working deployment or reproduce a private-data environment from the source snapshot alone.

## Update after development

Replace this current-state note with actual branch/commit, changes, checks and results, known issues, uncommitted work, decisions and next steps. Update PROJECT_CONTEXT.md when setup or architecture changes. State what remains unverified. Do not commit chat logs, credentials or unrelated personal data.
