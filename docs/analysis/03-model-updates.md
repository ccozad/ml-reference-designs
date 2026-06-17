# LLM Model Updates

Every hard-coded model string in the repo, what generation it represents, and how to bring it current. This is one of the easiest classes of cleanup — most are one-line edits — but a few cases require README rewrites because the modern equivalent won't fit on a mid-tier consumer GPU.

## Anthropic (Claude)

**Resolved 2026-05-08 (issue #28).** All Claude model strings standardized on `claude-sonnet-4-6`, and `llm/claude-3-5/` renamed to `llm/claude/` (version-agnostic) to avoid future per-release renames. The original audit table is preserved below for historical reference.

| File (audit-era path) | Audit-era model | Now (2026-06-17) | Notes |
| --- | --- | --- | --- |
| `llm/claude-3-5/hello-world/app.py` | `claude-3-5-sonnet-20240620` | `claude-sonnet-4-6` (now `llm/claude/hello-world/app.py`) | Folder renamed `claude-3-5/` → `claude/` (version-agnostic). |
| `llm/claude-3-5/tool-calling/app.py` | `claude-3-5-sonnet-20240620` | `claude-sonnet-4-6` (now `llm/claude/tool-calling/app.py`) | Same. |
| `llm/claude-3-5/tool-calling/README.md` | references `claude-3-5-sonnet-20240620` | `claude-sonnet-4-6` (now `llm/claude/tool-calling/README.md`) | Updated alongside code. |
| `lang-graph/travel-agent/zero_shot_agent.py` | `claude-3-sonnet-20240229` | `claude-sonnet-4-6` | Deprecated Claude 3 ID replaced. |
| `lang-graph/travel-agent/confirmation_agent.py` | `claude-3-sonnet-20240229` | `claude-sonnet-4-6` | Same. |
| `lang-graph/travel-agent/smart_confirm_agent.py` | `claude-3-sonnet-20240229` | `claude-sonnet-4-6` | Same. |
| `lang-chain/Neo4j/cypher_generation.py` | `claude-3-sonnet-20240229` | `claude-sonnet-4-6` | Same. |
| `mcp/client-py/client.py` | `claude-3-5-sonnet-20241022` (×2) | `claude-sonnet-4-6` (×2) | Same. |

**Recommendation**: standardize all Claude examples on the latest Claude 4.x Sonnet (or Haiku where cost matters — e.g. the dummy / chat-style demos). Add a small comment near each model string explaining what changes if the user wants to swap it out.

## OpenAI

**Resolved 2026-06-17.** Standardized on the current (June 2026) GPT-5.4 generation: cheap completion/RAG demos use `gpt-5.4-nano`, agentic/tool-using examples use `gpt-5.4` (with `gpt-5.4-mini` as the browser-use planner). `gpt-4o`/`gpt-4o-mini` were two generations behind by mid-2026, so the doc's original `gpt-4o-mini` recommendation was superseded. Files updated: `lang-chain/RAG`, `lang-chain/RAG-serve`, `lang-chain/docker-serve`, `lang-chain/Azure` (code + READMEs), `llama-index/llm/app.py`, `llama-index/citation-query-engine`, `lang-chain/fast-api` (enum + default), `browser-use/find_car_prices.py`, `browser-use/find_flights.py`. The original audit table is preserved below for historical reference.

| File | Audit-era model | Now (2026-06-17) | Notes |
| --- | --- | --- | --- |
| `lang-chain/RAG/rag_pipeline.py` | `gpt-3.5-turbo-0125` | `gpt-5.4-nano` | Cheap RAG demo. |
| `lang-chain/RAG/README.md` | mentions `gpt-3.5-turbo-0125` | `gpt-5.4-nano` | Updated alongside code. |
| `lang-chain/RAG-serve/custom_pipelines.py` | `gpt-3.5-turbo-0125` | `gpt-5.4-nano` | Cheap RAG demo. |
| `lang-chain/RAG-serve/README.md` | mentions `gpt-3.5-turbo-0125` | `gpt-5.4-nano` | Updated alongside code. |
| `lang-chain/docker-serve/custom_pipelines.py` | `gpt-3.5-turbo-0125` | `gpt-5.4-nano` | Cheap RAG demo. |
| `lang-chain/docker-serve/README.md` | mentions `gpt-3.5-turbo-0125` | `gpt-5.4-nano` | Updated alongside code. |
| `lang-chain/Azure/rag_pipeline.py` | `gpt-3.5-turbo-0125` | `gpt-5.4-nano` | Cheap RAG demo. |
| `llama-index/llm/app.py` | `gpt-3.5-turbo` | `gpt-5.4-nano` | Cheap completion demo. |
| `lang-chain/fast-api/pydantic_models.py` | enum `gpt-4o`, `gpt-4o-mini` | enum `gpt-5.4`, `gpt-5.4-nano` (default `gpt-5.4-nano`) | Selector enum bumped to current generation. |
| `lang-chain/fast-api/langchain_utils.py` | `gpt-4o-mini` default | `gpt-5.4-nano` default | Same. |
| `llama-index/citation-query-engine/citation_query_engine.py` | `gpt-4o-mini` | `gpt-5.4-nano` | Cheap demo. |
| `browser-use/find_car_prices.py` | `gpt-4o` | `gpt-5.4` | Agentic/tool-using → capable tier. |
| `browser-use/find_flights.py` | `gpt-4o` (planner `o3-mini`) | `gpt-5.4` (planner `gpt-5.4-mini`) | Agentic; deprecated `o3-mini` planner replaced. |

**Recommendation (superseded)**: the original advice was `gpt-4o-mini` for cheap demos / `gpt-4o`+ for tool-using. As of June 2026 the chosen default is `gpt-5.4-nano` for cheap demos and `gpt-5.4` for agentic/tool-using work.

## Meta (Llama)

**Resolved 2026-06-17.** Bumped `llm/llama-3/hello-world/` from `meta-llama/Meta-Llama-3-8B` to `meta-llama/Llama-3.1-8B` (code + README + model-card URL). This is the latest *dense 8B* Llama — Llama 3.2 has no 8B, Llama 3.3 is 70B-only, and Llama 4 is MoE — so the same-size bump keeps the existing AWS g5.xlarge hardware story intact. Folder left as `llama-3/` per decision (no version-agnostic rename). The `agents/dummy-agent/*` files stay on `meta-llama/Llama-3.2-3B-Instruct`. SmolLM (`slm/smollm2/`) was intentionally left on `SmolLM2-360M` — SmolLM3 only ships at ~3B, an ~8x hardware jump not worth it for the "runs anywhere" demo. The original audit table is preserved below for historical reference.

| File | Audit-era model | Now (2026-06-17) | Notes |
| --- | --- | --- | --- |
| `llm/llama-3/hello-world/hello.py` | `meta-llama/Meta-Llama-3-8B` | `meta-llama/Llama-3.1-8B` | Latest dense 8B; same g5.xlarge footprint, AWS README unchanged. |
| `llm/llama-3/hello-world/README.md` | references `Meta-Llama-3-8B` (×2) | `Llama-3.1-8B` (+ model-card URL) | Updated alongside code. |
| `agents/dummy-agent/*.py` (4 files) | `meta-llama/Llama-3.2-3B-Instruct` | unchanged | Already current small variant; good consumer-GPU fit. |

**Recommendation (partially applied)**: bumped to the latest 8B (`Llama-3.1-8B`) keeping the `llm/llama-3/` folder; the version-agnostic folder rename was declined. Llama 3.2 has no 8B, 3.3 is 70B-only, and Llama 4 is MoE, so 3.1 is the newest dense 8B.

## Microsoft (Phi)

**Resolved 2026-06-17.** Bumped `slm/phi-3/hello-world/` from `microsoft/Phi-3-mini-4k-instruct` to `microsoft/Phi-4-mini-instruct` (code + README). Phi-4-mini is 3.8B — the same size class as Phi-3-mini, so it runs on the same hardware; it supersedes the originally-recommended Phi-3.5-mini. The folder name (`phi-3/`) was left as-is. A separate larger `slm/phi-4/` (~14B) example remains a possible follow-up (GitHub issue #8). The original audit table is preserved below for historical reference.

| File | Audit-era model | Now (2026-06-17) | Notes |
| --- | --- | --- | --- |
| `slm/phi-3/hello-world/hello.py` | `microsoft/Phi-3-mini-4k-instruct` | `microsoft/Phi-4-mini-instruct` | Phi-4-mini is 3.8B — same size class, same hardware. |
| `slm/phi-3/hello-world/README.md` | references Phi-3 throughout | references Phi-4 | Updated alongside code. |

**Recommendation (applied, revised)**: the original advice was `Phi-3.5-mini-instruct`; by June 2026 `Phi-4-mini-instruct` is the current same-size (3.8B) successor, so that was used instead. A separate larger `slm/phi-4/` (~14B) example is still a possible follow-up (GitHub issue #8).

## Hugging Face (SmolLM)

**Reviewed 2026-06-17 — intentionally left as-is.** SmolLM3 only ships at ~3B, an ~8x jump from the 360M model; that breaks the "runs anywhere / even on a phone" point of this demo, so it stays on SmolLM2-360M.

| File | Audit-era model | Now (2026-06-17) | Notes |
| --- | --- | --- | --- |
| `slm/smollm2/story-writer/generate-story.py` | `HuggingFaceTB/SmolLM2-360M` | unchanged | SmolLM3 (~3B) is too large for the tiny-model demo; 360M kept deliberately. |

**Recommendation (declined)**: bumping to SmolLM3 was considered and declined — the hardware jump outweighs the benefit for this example.

## Hardware caveat

The README disclaimer ("some examples can't be fully updated because the latest language models won't fit on my mid tier consumer graphics card") is real and worth preserving. The pragmatic split is:

- **Hosted API examples** (Claude, OpenAI, Bedrock) — always upgrade to the latest model; cost is the only concern.
- **Local model examples** (Llama, Phi, SmolLM) — pick the largest variant that fits on a 12 GB consumer GPU. Document the VRAM footprint and the smaller fallback.

## Suggested issue grouping

- **One issue per provider** (Anthropic, OpenAI, Llama-local, Phi-local, SmolLM-local), not one issue per file. This avoids 15 trivial PRs and keeps the model-choice discussion in one place per provider.
- The Llama and Phi issues should explicitly include "rewrite the hardware paragraph in the README" as part of the work.
