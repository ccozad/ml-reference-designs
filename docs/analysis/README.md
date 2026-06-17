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

## Verification tracking

The model-string updates ([03-model-updates.md](./03-model-updates.md)) have been applied to code and READMEs but **not yet verified end-to-end**. A large verification pass is planned; it is tracked by one GitHub issue per model vendor (label `verification`, milestone **2026 Cleanup**):

| Vendor | Issue | What to confirm |
| --- | --- | --- |
| OpenAI | [#51](https://github.com/ccozad/ml-reference-designs/issues/51) | RAG / llama-index / fast-api on `gpt-5.4-nano`; browser-use on `gpt-5.4` |
| Anthropic | [#52](https://github.com/ccozad/ml-reference-designs/issues/52) | claude / travel-agent / Neo4j / mcp on `claude-sonnet-4-6` |
| Meta (Llama) | [#53](https://github.com/ccozad/ml-reference-designs/issues/53) | hello-world on `Llama-3.1-8B` (gated); dummy-agent on `Llama-3.2-3B` |
| Microsoft (Phi) | [#54](https://github.com/ccozad/ml-reference-designs/issues/54) | phi hello-world on `Phi-4-mini-instruct` |
| Hugging Face (SmolLM) | [#55](https://github.com/ccozad/ml-reference-designs/issues/55) | story-writer on `SmolLM2-360M` (unchanged) |

## Scope

This analysis began as a descriptive snapshot (2026-05-08) — the original audit changed no code. Since then the README-fix and model-update cleanup items **have been applied** (see the "Resolved" notes in each document); the remaining gate is the runtime verification pass tracked above. New work is still filed against the **2026 Cleanup** milestone.
