# New Topic Ideas

Candidates for new examples, organized by theme. Each entry notes what's already in the repo, what's new, and why it would slot in well. Existing GitHub issues that already capture an idea are noted; this list extends rather than duplicates them.

## High priority — fills a 2026-shaped gap

### Anthropic / Claude API features beyond basic chat
The repo has Claude 3.5 hello-world and tool-calling. The Claude API has matured significantly since then with features that are easy to demo and high-value:
- **Prompt caching** — show the cost / latency delta on a long-context document Q&A workload
- **Extended thinking** — visible reasoning tokens; pair with a math or planning task
- **Citations** — first-class support for grounded answers; complements the existing LlamaIndex citation example
- **Files API** — upload a PDF and ask questions, no manual chunking

### Claude Agent SDK
The repo has SmolAgents (HuggingFace), LangGraph, and OpenAI Agents examples. Adding Anthropic's Agent SDK would round out the major SDK comparison. Issue #22 covers A2A; this is adjacent but distinct.

### Multimodal vision
Currently the repo's "image" content is OpenCV preprocessing, classification, and segmentation — all classical/specialized models. There's no example of "send an image to a frontier model and ask about it". Easy demo: receipt processing (already listed as a domain), document OCR, chart extraction.

### LLM evaluation / "LLM as judge"
The repo has lots of generation examples but no measurement examples. A simple `evals/` section with one of:
- Pairwise A/B with a judge model
- Reference-based scoring on a small dataset
- Automated regression test for a RAG pipeline (e.g. RAGAS or DeepEval)

This pairs naturally with the existing RAG content as "now how do you tell if it's actually good?"

### Reranking and hybrid search
RAG content currently stops at "embed + retrieve top-k". A small example of:
- Hybrid BM25 + dense
- A cross-encoder reranker on top of dense retrieval

would directly improve retrieval quality and make the existing RAG pipelines noticeably better.

### Fine-tuning a small model
LoRA / QLoRA on a 3B-class model that fits on a 12 GB consumer GPU. Pairs with the existing SmolLM and Phi examples. Could use TRL's `SFTTrainer` for simplicity. A second variant doing DPO on the same model would be a natural follow-up.

## Medium priority — fills out an existing section

### MCP — more server examples
Existing: Python client, .NET server, Python weather server (unlinked), Gradio MCP hello-world (unlinked). Once the unlinked items are surfaced, the natural next additions are:
- MCP server backed by a real database (sqlite/postgres) with auth
- MCP server that wraps an existing API (GitHub, Slack)
- MCP transport variations: stdio vs HTTP vs SSE

### Agent observability
Trace screenshot is already in the repo for OpenAI's Trace UI. Adding an example with Langfuse or Arize Phoenix would broaden coverage and is genuinely useful for anyone building agents in production.

### Vector store comparison
Currently uses Chroma in most places, AWS Bedrock vector and Azure AI Search variants exist. A side-by-side `pgvector` example would round out the "managed vs self-hosted" story. Qdrant is another natural addition.

### GraphRAG
There's a basic Neo4j example. The interesting modern variant is GraphRAG-style "build a knowledge graph from documents, then traverse it during retrieval." Microsoft's GraphRAG and the LlamaIndex KnowledgeGraphIndex are both demoable.

### Speech / voice
The audio-agent example is a great start. Natural follow-ups:
- Whisper transcription standalone (not embedded in an agent)
- TTS via ElevenLabs or OpenAI TTS as a standalone

### Image generation
Repo has zero image-generation content. A small `diffusers/` example using Flux or SDXL would slot in alongside the existing diffusion-from-scratch placeholder (issue #6).

## Lower priority / nice-to-have

- **DSPy or Pydantic AI** — alternative agent / prompting frameworks
- **LiteLLM / OpenRouter** — model routing demo, useful as a "swap providers without rewriting code" example
- **Time-series with deep models** — Prophet → N-BEATS → Time-LLM progression
- **Anomaly detection** — Isolation Forest + autoencoder pair, fills a glaring gap
- **Recommender systems** — at least a simple matrix factorization demo
- **Quantization** — GGUF / AWQ / GPTQ for the local-model examples; directly addresses the "fits on consumer GPU" constraint
- **ONNX export + inference** — bridges the PyTorch examples to a deployment story

## What's already tracked

These already have open issues; the analysis confirms they're still relevant:

- #3 Sapiens, #5 OpenLRM, #6 diffuser-from-scratch, #7 CrewAI, #8 Phi 4, #9 PDF RAG, #10 Sagemaker, #11 Azure ML, #15 facial recognition, #16 Apache Hop, #18 FastAPI (item exists already; just needs linking — see `05-unlinked-content.md`), #19 retrieval agents, #21 HF Transformers, #22 A2A, #23 Docker, #24 LeRobot

## Suggested approach

Treat the high-priority list as candidate cleanup-milestone work; let the medium / lower-priority items stay as ideas until a specific need shows up. New issues should be filed only for the high-priority items so the milestone stays focused.
