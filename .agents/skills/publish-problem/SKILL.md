---
name: publish-problem
description: Publish completed NeatCode150 problem changes through a guarded GitHub workflow. Use only when the user explicitly invokes $publish-problem or clearly requests the entire test, feature-branch, commit, push, draft pull request, review, approval, merge, synchronization, and branch-cleanup sequence. Stop before approval or merge when a major review issue or test failure is found.
---

# Publish Problem

Publish one completed problem from the NeatCode150 repository. Treat explicit invocation as authorization for the full workflow below, subject to platform approvals and the stop conditions in this skill.

## Establish Scope

1. Resolve the Git root and confirm it is the intended NeatCode150 repository.
2. Read the applicable `AGENTS.md` and repository documentation.
3. Inspect `git status -sb`, all unstaged and staged diffs, untracked files, recent commits, the current branch, remotes, and the remote default branch.
4. Identify the intended problem source file, matching test file, and README changes from filenames and diff content.
5. Exclude unrelated or generated files, including `.DS_Store`, `__pycache__`, `*.pyc`, caches, virtual environments, editor settings, and build output.
6. If multiple unrelated changes or problems are present and the intended scope cannot be proven, stop and ask the user which files belong. Never use `git add -A` in a mixed worktree.

Verify that the base branch is synchronized with its remote before creating the feature branch. If local `main` is ahead, behind, diverged, or contains unpublished work outside the intended scope, stop and report the condition rather than creating a contaminated branch.

## Verify Prerequisites

1. Confirm Git and GitHub CLI availability.
2. Confirm GitHub authentication and access to `origin`.
3. Determine the base branch from the remote; use `main` when it is the repository default.
4. Determine the focused and full test commands from repository configuration and existing practice.
5. Stop without committing if authentication, remote access, or base synchronization cannot be established.

## Create the Feature Branch

Create a concise, meaningful branch from the synchronized base branch. Prefer:

```text
feature/<problem-slug>
```

Never use `codex/`, `agent/`, or a vague generated prefix. If already on a suitable feature branch containing only the intended work, retain it.

## Test Before Committing

1. Run the focused tests for the problem.
2. Run any executable examples or problem-specific checks used by the repository.
3. Run the complete test suite.
4. Record commands, pass/fail counts, and relevant output.
5. If any required test fails, stop before commit and push. Report the failure and the required fix.

Do not install new project dependencies or alter application code merely to make the publishing workflow pass unless the user separately authorizes that change.

## Stage and Commit

1. Stage only the confirmed source, test, and documentation files using explicit paths.
2. Inspect the cached diff and run `git diff --cached --check`.
3. Confirm no excluded or unrelated file is staged.
4. Commit with a concise problem-specific message, such as `Add valid binary search tree solution`.
5. Capture the full commit hash and exact subject.

## Push and Open a Draft Pull Request

1. Push the feature branch to `origin` with upstream tracking.
2. Open a draft pull request targeting the remote default branch.
3. Use a clear problem-specific title.
4. Include real Markdown sections covering:
   - Summary
   - Implementation details
   - Focused test results
   - Full-suite results
5. Capture the pull-request URL and number.

## Review the Complete Pull-Request Diff

Review the entire base-to-head diff, not only the last commit. Evaluate:

- Correctness and agreement with the requested approach
- Accidental solution or documentation changes
- Edge cases and input boundaries
- Complexity claims and unnecessary complexity
- Maintainability, naming, and repository conventions
- Test quality and coverage
- Generated, secret, or unrelated files

Classify findings as:

- **Major:** incorrect behavior, failing required tests, destructive or insecure behavior, contaminated scope, missing essential coverage, or a change that should block merge
- **Minor:** non-blocking maintainability, clarity, or coverage improvement

If any major finding exists, do not mark the pull request ready, approve it, merge it, or delete branches. Report the finding and recommend the required fix.

## Complete a Clean Review

Only when required tests pass and no major finding exists:

1. Mark the draft pull request ready for review.
2. Approve it when GitHub permits approval by the authenticated account. If self-approval is prohibited, record that outcome without treating it as a failure.
3. Merge using the repository's supported merge method.
4. Capture the resulting merge commit hash from the updated remote base branch.
5. Switch the local checkout to the base branch.
6. Fetch and fast-forward it from `origin/<base>` using a fast-forward-only operation.
7. Confirm local base and remote base resolve to the same commit.
8. Delete the feature branch locally only after leaving it and confirming the merge.
9. Delete the remote feature branch only after confirming the merged state.
10. Verify the final working tree is clean. Preserve unrelated user work if it existed before the workflow; never discard it to achieve a clean status.

## Final Report

Report:

- Feature branch name
- Commit hash and message
- Files included in the commit
- Focused and full test results
- Pull-request URL
- Review findings by severity
- Ready-for-review status
- Approval status and any self-approval restriction
- Merge status and merge commit hash
- Local and remote branch-cleanup status
- Final local branch
- Local/remote synchronization status
- Any preserved unrelated changes or blockers
