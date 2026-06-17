# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A personal reference vault and shareable demo collection of small, **self-contained** ML/AI examples — not a single application. Each example lives in its own leaf folder (e.g. `agents/code-agents/`, `llm/claude/hello-world/`, `lang-chain/RAG/`) and stands alone with its own `requirements.txt`, `.venv`, `README.md`, and (where credentials are needed) `.env`. The top-level `README.md` is the curated index linking out to every example, grouped by topic.

There is **no test suite, no CI, and no top-level build.** Changes are validated by running the individual example. Treat each leaf folder as the unit of work.

## Running a Python example

Every Python example uses the same per-folder virtualenv workflow, documented once in `docs/setup/python-venv.md` and linked from each README. From the example's own directory (the one containing its `requirements.txt`):

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip3 install -r requirements.txt
python3 <script_name>.py         # or: jupyter notebook <file>.ipynb
deactivate
```

The **root `requirements.txt`** is only for the older notebook/data-science content (PyTorch, OpenCV, scikit-learn, TensorFlow notebooks under `general/`, `opencv/`, `pytorch/`, etc.). Standalone-script examples ignore it and use their own folder-local `requirements.txt`.

### Credentials

Examples that call hosted models read tokens from a folder-local `.env` (gitignored). The variable name depends on the provider the example uses — `ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, or `HF_TOKEN`. Check the example's README for which one it expects.

### The one .NET example

`mcp/dotnet/MyFirstMCP/` is a C# MCP server (`dotnet run` in that folder); `ml-reference-designs.sln` exists only to open it in Visual Studio. Everything else in the repo is Python.

## Conventions to follow when adding or editing examples

- **New examples are leaf folders** containing `requirements.txt`, a `README.md`, the script(s), and any data. Add a link to the new example under the appropriate topic heading in the top-level `README.md` — content that exists but isn't linked there is treated as incomplete/abandoned (see `docs/analysis/05-unlinked-content.md`).
- **README structure** mirrors existing examples: a Dependencies section (required token + a link to `docs/setup/python-venv.md` rather than re-pasting the venv steps), then a "Run the code" section that shows the command and a sample of its console output. Do not duplicate the venv boilerplate inline — link the central doc.
- **Use current model strings.** Claude examples target `claude-sonnet-4-6` (or the latest appropriate Claude model — consult the `claude-api` skill before hardcoding). Older `llm/claude-3-5/` style folders are superseded by `llm/claude/`. When updating a model, note any hardware constraints in the README instead of upgrading silently.
- Path/name copy-paste bugs in READMEs are a known recurring issue — when you fork an example's README, fix the directory names and any `<...>` placeholders.

## Repository map

- `agents/` — agent patterns (SmolAgents, OpenAI Agents): dummy, code, workout, retrieval, multi-agent, audio
- `llm/`, `slm/` — direct LLM/SLM calls (Claude, Llama 3, Phi-3, SmolLM2): hello-world and tool-calling
- `lang-chain/`, `lang-graph/`, `llama-index/` — framework-specific RAG, serving, and graph/agent flows
- `mcp/` — Model Context Protocol servers/clients (Python and one .NET)
- `browser-use/`, `diffuser/`, `segment-anything-model/`, `gradio/`, `huggingface/`, `opencv/` — task/library-specific demos
- `pytorch/`, `tensor-flow/`, `scikit-learn/`, `general/` — notebook-based getting-started, feature-engineering, regression, and classification recipes
- `docs/setup/` — shared setup docs (the venv workflow); `docs/analysis/` — a 2026 cleanup audit and roadmap (notebook→script conversion, model updates, README fixes, coverage gaps). Consult `docs/analysis/` before large cleanup work to align with the planned sequencing.
