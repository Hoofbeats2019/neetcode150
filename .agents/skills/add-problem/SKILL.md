---
name: add-problem
description: Add or scaffold a programming problem in the NeatCode150 repository from a problem number, title, statement or URL, and optional user pseudocode. Use when the user asks to add a NeetCode or LeetCode problem, create its solution and test files, follow existing problem examples, or update the repository README for a new problem. Support scaffold-only and user-directed implementation modes while preserving the tutoring rules in AGENTS.md.
---

# Add Problem

Add one programming problem while treating the repository as the source of truth for structure and style.

## Gather Inputs

Identify these inputs from the request:

- Problem number, when supplied
- Problem title
- Problem statement or URL
- User pseudocode or proposed approach
- Mode: `scaffold` or `implement`

If the title or problem behavior is missing, ask for it. If only a URL is supplied, retrieve the statement when access is available; otherwise ask the user to paste it.

Default to `scaffold` when the user does not explicitly request implementation or when their pseudocode is insufficient. Never invent the missing algorithm. Treat requests such as "implement my pseudocode" or "complete the solution" as `implement` mode.

## Inspect the Repository

1. Resolve the repository root with Git and confirm it is the intended NeatCode150 checkout.
2. Read the applicable `AGENTS.md` and the root `README.md`.
3. Inspect the working tree before editing. Preserve unrelated changes and ignore generated files.
4. Inspect at least two similar completed problems, including their matching files under `solutions/` and `tests/`. Prefer examples from the same category and data structure.
5. Derive naming, signatures, documentation, test style, README placement, and commands from those examples rather than assuming a fixed template.

## Plan the Change

Determine:

- The NeetCode category
- A snake_case module name based on the problem title
- `solutions/<module_name>.py`
- `tests/test_<module_name>.py`
- The appropriate row and learning-notes location in `README.md`

Before editing, check that the target files and README entry do not already exist. If they do, update the existing problem only when the request clearly calls for it; otherwise report the conflict.

## Create the Problem Files

Follow the conventions discovered in the inspected examples.

For both modes:

- Include the problem description, supplied examples, constraints, expected class or data structures, and callable signature in the solution module.
- Add executable example-test scaffolding to the solution module when that is the repository convention.
- Create a matching `unittest` module covering supplied examples and reasonable edge cases that follow directly from the statement.
- Do not copy editorial solutions or introduce an approach the user did not provide.

For `scaffold` mode:

- Create imports, required types, class definitions, method signatures, docstrings, and explicit TODO markers only.
- Leave the algorithm unimplemented in a clear, syntactically valid way.
- Do not mark the README entry as solved and do not claim final complexity.

For `implement` mode:

- Translate only the user's pseudocode or approved approach into code.
- Keep the implementation proportional to that pseudocode.
- If the pseudocode has a correctness gap, stop at the smallest useful scaffold or code fragment, explain the gap, and request clarification instead of silently replacing the approach.
- Add edge-case tests without disclosing a different complete algorithm.

## Update Documentation

Update every relevant location in the root `README.md` while preserving its formatting and ordering:

- Add or update the progress-table row with the problem link, category, status, approach, time complexity, and space complexity.
- Use `In Progress` and `TBD` values for unimplemented or unverified scaffolds.
- Use `Solved` and concrete complexity values only after the requested implementation is complete and focused tests pass.
- Add concise learning notes derived from the user's pseudocode or completed implementation. Do not reveal an unrequested full solution through the notes.

## Validate

1. Review the complete diff for unintended edits, naming mismatches, stale README links, and accidental solution disclosure.
2. Run the new solution module's executable examples when implemented.
3. Run the focused unit-test module using the repository's existing test runner.
4. For a scaffold, run the safest useful syntax or import validation and clearly report tests that are expected to remain incomplete.
5. Do not run the full suite unless requested or necessary to check a shared-code change.
6. Remove no user files. Never stage `.DS_Store`, `__pycache__`, `*.pyc`, test caches, virtual environments, or unrelated changes.

## Report

Summarize:

- Mode used
- Files created
- Files updated
- README changes
- Focused tests or checks and their results
- Assumptions
- Unresolved questions or expected scaffold failures

Do not commit, push, or open a pull request unless the user separately requests publication.
