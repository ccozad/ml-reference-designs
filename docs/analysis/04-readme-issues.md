# README Path & Instruction Issues

The per-example READMEs were largely produced by copy-pasting a boilerplate setup section between folders, then editing inconsistently. This document lists the bugs that block a new reader from following along, grouped by kind.

## Bugs that point readers to the wrong directory

These are the ones that actively send a reader running `cd <wrong/path>`:

- **`agents/audio-agent/README.md`** says "Move to the multi-agents folder / `cd <agents/audio-agent>`". The label is wrong; the path is right. Fix the prose.
- **`lang-graph/travel-agent/README.md`** says "Move to the workout-agents folder / `cd <lang-graph/travel-agent>`". Same shape — wrong label, right path.
- **`slm/phi-3/hello-world/README.md`** says "Move to the llm\\phi-3\\hello-world folder / `cd <slm\\phi-3\\hello-world>`". The first path is wrong (`llm` should be `slm`); the second is right.

## Typos and minor errors

- **`llama-index/citation-query-engine/README.md`** has `OPENAI_API_KEY=your token>` — the leading `<` is missing.
- **`lang-chain/Azure/rag_pipeline.py`** sample output in the README mentions "Initializing Bedrock client...". This is leftover from the AWS Bedrock example; the Azure version doesn't talk to Bedrock.
- **`lang-chain/Azure/README.md`** lists `OPENAI_API_KEY` in the env-var block but the dependencies section doesn't explain why an OpenAI key is needed alongside Azure AI Search. Add a one-liner or remove the env var if the example is fully Azure-native.
- **`llm/claude-3-5/tool-calling/README.md`** has the line "At it's core" — should be "At its core". Minor.

## Empty / abandoned

- **`agents/batch-agents/README.md`** is **0 bytes**. The directory contains `tools/batch.py`, `tools/sentiment.py`, `tools/final_answer.py`, and a `requirements.txt` but no entry point. Either flesh out into a real example or delete the folder.

## Inconsistent path style

Most READMEs render Unix-style paths (`agents/code-agents`) but a few of the Windows-targeted examples mix slashes:

- `slm/phi-3/hello-world/README.md` — uses `llm\\phi-3\\hello-world` and `<slm\\phi-3\\hello-world>` in the same block
- `slm/smollm2/story-writer/README.md` — uses `slm\\smollm2\\story-writer`

Recommend standardizing on forward slashes everywhere for portability; Windows shells accept them.

## Duplicated boilerplate

The following block appears verbatim (modulo the folder name) in roughly 25 READMEs:

```
## Python Virtual Environment

 - Move to the <X> folder
   - `cd <X>`
 - Create a virtual environment
   - On Mac: `python3 -m venv .venv`
   - On Windows: `python -m venv .venv`
 - Activate the virtual environment
 ...
```

This is the source of the "wrong folder name" bugs above — a small typo in one folder doesn't propagate to others, and a fix in one folder doesn't propagate either.

Two options:

1. **Centralize**: move the block to a single doc (e.g. `docs/setup/python-venv.md`) and have each per-example README link to it with a one-line "Set up a virtualenv ([instructions](../../docs/setup/python-venv.md)), then …".
2. **Normalize**: keep the per-folder copies but enforce a stable wording. Less ideal because future copy-pastes will still drift.

Option 1 is more work up front but eliminates a recurring class of bug.

## Top-level README touch-ups (optional)

- The "Working with LLMs" → "Llama 3" subsection at the bottom assumes the user is downloading weights for the AWS EC2 example. The link to `https://huggingface.co/meta-llama/Meta-Llama-3-8B` is fine but pairs awkwardly with the per-example README. Consider deleting that subsection and letting the per-example README own it.
- The "Setup → Windows" snippet pins `cu118` for PyTorch. CUDA 12.x has been shipping for a long time; revisit when the model upgrade work happens.

## Suggested issue grouping

- **One issue** for the wrong-folder typos + the citation-query-engine env-var typo (small, all in the same vein).
- **One issue** for the empty `agents/batch-agents/` folder (decide: build out or delete).
- **One issue** for centralizing the venv boilerplate (bigger change, worth its own discussion).
