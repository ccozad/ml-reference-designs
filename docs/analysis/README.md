# 2026 Repo Analysis

A snapshot review of `ml-reference-designs` performed on 2026-05-08 to drive the **2026 Cleanup** milestone.

The repo's stated purpose is to provide a personal reference vault and shareable demo collection for common ML / AI tasks. The analysis below identifies friction that gets in the way of that goal, then proposes a punch list of concrete cleanup items and a forward-looking list of new topics worth adding.

## Documents

1. [Overview & summary](./01-overview.md) — top findings and recommended sequencing
2. [Notebooks → standalone Python](./02-notebook-conversion.md) — full notebook inventory and conversion plan
3. [Model version updates](./03-model-updates.md) — every hard-coded LLM model string, what to migrate to, and hardware caveats
4. [README issues](./04-readme-issues.md) — copy-paste errors, broken paths, and inconsistent setup instructions
5. [Unlinked / incomplete content](./05-unlinked-content.md) — directories present in the repo but missing from the top-level README
6. [New topic ideas](./06-new-topic-ideas.md) — candidate additions, prioritized

## Scope

This analysis is descriptive — no code or examples were changed. The output is a set of GitHub issues filed against the **2026 Cleanup** milestone so the work can be picked up incrementally in future sessions.
