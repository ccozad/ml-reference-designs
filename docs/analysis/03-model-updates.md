# LLM Model Updates

Every hard-coded model string in the repo, what generation it represents, and how to bring it current. This is one of the easiest classes of cleanup — most are one-line edits — but a few cases require README rewrites because the modern equivalent won't fit on a mid-tier consumer GPU.

## Anthropic (Claude)

**Resolved 2026-05-08 (issue #28).** All Claude model strings standardized on `claude-sonnet-4-6`, and `llm/claude-3-5/` renamed to `llm/claude/` (version-agnostic) to avoid future per-release renames. The original audit table is preserved below for historical reference.

| File | Current model | Notes |
| --- | --- | --- |
| `llm/claude-3-5/hello-world/app.py` | `claude-3-5-sonnet-20240620` | Folder name is `claude-3-5/`. Consider renaming the folder to `claude-4/` (or `claude/` and version-agnostic) to avoid a recurring rename every release. |
| `llm/claude-3-5/tool-calling/app.py` | `claude-3-5-sonnet-20240620` | Same as above. |
| `llm/claude-3-5/tool-calling/README.md` | references `claude-3-5-sonnet-20240620` | Update text alongside code. |
| `lang-graph/travel-agent/zero_shot_agent.py` | `claude-3-sonnet-20240229` | This Claude 3 (not 3.5) Sonnet ID is **deprecated**. |
| `lang-graph/travel-agent/confirmation_agent.py` | `claude-3-sonnet-20240229` | Same. |
| `lang-graph/travel-agent/smart_confirm_agent.py` | `claude-3-sonnet-20240229` | Same. |
| `lang-chain/Neo4j/cypher_generation.py` | `claude-3-sonnet-20240229` | Same. |
| `mcp/client-py/client.py` | `claude-3-5-sonnet-20241022` (×2) | Newer than the others but still a generation behind. |

**Recommendation**: standardize all Claude examples on the latest Claude 4.x Sonnet (or Haiku where cost matters — e.g. the dummy / chat-style demos). Add a small comment near each model string explaining what changes if the user wants to swap it out.

## OpenAI

| File | Current model | Notes |
| --- | --- | --- |
| `lang-chain/RAG/rag_pipeline.py` | `gpt-3.5-turbo-0125` | Upgrade to `gpt-4o-mini` at minimum; the cost delta is negligible and quality is much better for RAG. |
| `lang-chain/RAG/README.md` | mentions `gpt-3.5-turbo-0125` | Update text alongside code. |
| `lang-chain/RAG-serve/custom_pipelines.py` | `gpt-3.5-turbo-0125` | Same. |
| `lang-chain/RAG-serve/README.md` | mentions `gpt-3.5-turbo-0125` | Same. |
| `lang-chain/docker-serve/custom_pipelines.py` | `gpt-3.5-turbo-0125` | Same. |
| `lang-chain/docker-serve/README.md` | mentions `gpt-3.5-turbo-0125` | Same. |
| `lang-chain/Azure/rag_pipeline.py` | `gpt-3.5-turbo-0125` | Same. |
| `llama-index/llm/app.py` | `gpt-3.5-turbo` | Same. |
| `lang-chain/fast-api/pydantic_models.py` | enum `gpt-4o`, `gpt-4o-mini` | Current as of mid-2024; revisit once the repo settles on a default. |
| `lang-chain/fast-api/langchain_utils.py` | `gpt-4o-mini` default | Same. |
| `llama-index/citation-query-engine/citation_query_engine.py` | `gpt-4o-mini` | Same. |
| `browser-use/find_car_prices.py` | `gpt-4o` | Current; revisit when standardizing. |
| `browser-use/find_flights.py` | `gpt-4o` | Same. |

**Recommendation**: pick a single default tier (e.g. `gpt-4o-mini` for cheap demos, `gpt-4o` or newer for anything tool-using) and apply it consistently. Document the choice once in the top-level README so per-example READMEs don't have to repeat the rationale.

## Meta (Llama)

| File | Current model | Notes |
| --- | --- | --- |
| `llm/llama-3/hello-world/hello.py` | `meta-llama/Meta-Llama-3-8B` | The README is built around a g5.xlarge AWS EC2 instance; that's still fine, but Llama 3 has been superseded by Llama 3.1 / 3.2 / 3.3. The 8B size will not fit comfortably on a mid-tier consumer GPU (8–12 GB VRAM); call this out explicitly in the README. |
| `llm/llama-3/hello-world/README.md` | references `Meta-Llama-3-8B` (×2) | Update text alongside code. |
| `agents/dummy-agent/*.py` (4 files) | `meta-llama/Llama-3.2-3B-Instruct` | Already Llama 3.2 and a small variant — **leave as-is** or bump to Llama 3.3 once that's released in a 3B size. Good consumer-GPU fit. |

**Recommendation**: rename the `llm/llama-3/` folder to something version-agnostic (`llm/llama/`) and pick the latest 8B or 70B target. For a "fits on consumer hardware" story, prefer Llama 3.2-3B in any new content.

## Microsoft (Phi)

| File | Current model | Notes |
| --- | --- | --- |
| `slm/phi-3/hello-world/hello.py` | `microsoft/Phi-3-mini-4k-instruct` | Phi-3.5 and Phi-4 have shipped since this was written. Phi-3.5-mini has the same parameter footprint and runs on the same hardware; Phi-4 is larger (~14B). |
| `slm/phi-3/hello-world/README.md` | references Phi-3 throughout | Update text alongside code. |

**Recommendation**: bump to `microsoft/Phi-3.5-mini-instruct` for a same-size upgrade, or add a separate `slm/phi-4/` example as a "what does the next size up look like?" comparison. The original GitHub issue #8 (Add Phi 4 example) covers this.

## Hugging Face (SmolLM)

| File | Current model | Notes |
| --- | --- | --- |
| `slm/smollm2/story-writer/generate-story.py` | `HuggingFaceTB/SmolLM2-360M` | SmolLM3 has shipped. SmolLM2 still works fine for the demo. |

**Recommendation**: bump to SmolLM3 in a follow-up; lower priority than the Anthropic/OpenAI changes.

## Hardware caveat

The README disclaimer ("some examples can't be fully updated because the latest language models won't fit on my mid tier consumer graphics card") is real and worth preserving. The pragmatic split is:

- **Hosted API examples** (Claude, OpenAI, Bedrock) — always upgrade to the latest model; cost is the only concern.
- **Local model examples** (Llama, Phi, SmolLM) — pick the largest variant that fits on a 12 GB consumer GPU. Document the VRAM footprint and the smaller fallback.

## Suggested issue grouping

- **One issue per provider** (Anthropic, OpenAI, Llama-local, Phi-local, SmolLM-local), not one issue per file. This avoids 15 trivial PRs and keeps the model-choice discussion in one place per provider.
- The Llama and Phi issues should explicitly include "rewrite the hardware paragraph in the README" as part of the work.
