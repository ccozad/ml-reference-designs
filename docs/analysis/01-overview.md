# Overview & Summary

## Repo at a glance

- **20 Jupyter notebooks** spread across `general/`, `opencv/`, `pytorch/`, `scikit-learn/`, `tensor-flow/`, and one in `llm/llama-3/`
- **~75 standalone Python scripts** across agents, lang-chain, lang-graph, llama-index, llm, slm, mcp, browser-use, gradio, diffuser, segment-anything-model
- **30+ READMEs**, mostly per-example, plus the top-level `README.md`
- **18 open issues** already on GitHub, none yet attached to a 2026 milestone

## Top findings

1. **The notebook portion of the repo is now the minority.** The agent / LLM / RAG content is all standalone Python and dominates the repo. Converting the remaining notebooks to scripts is mostly mechanical and would make the repo internally consistent.
2. **Model strings are 1–2 generations out of date.** The Anthropic examples target `claude-3-sonnet-20240229` and `claude-3-5-sonnet-20240620`, OpenAI examples target `gpt-3.5-turbo-0125` / `gpt-4o`, the Llama example targets `Meta-Llama-3-8B`, and the Phi example targets `Phi-3-mini-4k-instruct`. As of early 2026 these all have current replacements (see `03-model-updates.md`). Some replacements have hardware constraints worth calling out in READMEs rather than just upgrading silently.
3. **Several READMEs were copy-pasted and have wrong directory names.** Examples: travel-agent README says "Move to the workout-agents folder", phi-3 README says "Move to the llm\\phi-3\\hello-world folder" (should be `slm`), audio-agent README says "Move to the multi-agents folder", citation-query-engine README has `OPENAI_API_KEY=your token>` (missing the leading `<`).
4. **The boilerplate "Python Virtual Environment" block is duplicated verbatim in ~25 READMEs.** This is the source of most of the path bugs — an edit to one rarely propagates. Consider extracting it to a single doc and linking, or normalizing the wording.
5. **Several directories are present but unlinked from the top-level README.** `agents/batch-agents/` (empty README, looks abandoned), `diffuser/`, `lang-chain/fast-api/`, `lang-chain/Azure/`, `lang-graph/tool-calling/`, `mcp/gradio/hello-world/`, `mcp/weather-server-py/`, `gradio/simple-ui/`, plus `browser-use/find_flights.py` and `agents/multi-agents/park_planner_agent.py`. Some are intentionally hidden because they're incomplete; others are finished and just missed when the index was last updated.
6. **Domain coverage is broad but has obvious 2026-era gaps.** Multimodal/vision via Claude or GPT-4o, prompt caching, extended thinking, evals, fine-tuning (LoRA/PEFT/DPO), reranking, GraphRAG beyond a single Neo4j example, agent observability (Langfuse/Arize), and Anthropic's Agent SDK are all common requests that would slot in naturally. See `06-new-topic-ideas.md`.

## Recommended sequencing

Order matters because some cleanup unlocks the rest:

1. **Fix README boilerplate bugs first** (low effort, high impact for anyone trying to follow along) — `04-readme-issues.md`
2. **Hide or delete the empty/abandoned content** so the repo's surface area matches what actually works — `05-unlinked-content.md`
3. **Update model strings**, splitting work into "swap the string" vs "may not run on consumer GPU, needs README rewrite" — `03-model-updates.md`
4. **Convert notebooks in batches by section** (PyTorch getting-started → home-prices → fashion-mnist; OpenCV; etc.) — `02-notebook-conversion.md`
5. **Add new topics** once the existing surface is stable — `06-new-topic-ideas.md`

## What this analysis intentionally does *not* cover

- Whether each example still actually runs end-to-end. Verifying execution is a per-issue task and depends on credentials/hardware.
- A line-by-line code review. The focus here is on structural cleanup, not refactoring.
- Changes to commit / PR conventions, CI, or testing — none currently exist and adding them is out of scope for "cleanup".
