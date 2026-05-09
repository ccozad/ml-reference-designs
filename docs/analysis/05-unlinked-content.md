# Unlinked / Incomplete Content

Content that exists in the repo but isn't surfaced from the top-level `README.md`. The repo's stated convention is that incomplete work stays unlinked, which is fine — but a few of these look complete and were probably just missed when the index was last updated, while others are clearly abandoned and should be removed to reduce surface area.

## Unlinked but appears complete (consider linking)

- **`gradio/simple-ui/`** — has README, `app.py`, `requirements.txt`. Looks like a working "hello Gradio" demo. **Recommend**: add to the README under a new "UI" or "Frontend" section, alongside Gradio mentions already present in agents.
- **`mcp/gradio/hello-world/`** — has README, `app.py`, `requirements.txt`. Another working demo, complements the existing MCP examples. **Recommend**: add under the existing "Deployment" section's MCP bullets.
- **`mcp/weather-server-py/`** — has README, `src/weather/server.py`, `requirements.txt`. Pairs naturally with `mcp/client-py/` (already linked). **Recommend**: link.
- **`lang-chain/fast-api/`** — has README, full FastAPI service (`main.py`, `chroma_utils.py`, `db_utils.py`, `langchain_utils.py`, `pydantic_models.py`). Was tracked by issue #18. **Recommend**: link under "Deployment" alongside the existing `RAG-serve` (Flask) and `docker-serve` examples — having Flask, Docker, and FastAPI variants side-by-side is genuinely useful for comparison.
- **`lang-chain/Azure/`** — has README, `index_pipeline.py`, `rag_pipeline.py`, `create_index.py`. The README has a stale "Bedrock" output example (see `04-readme-issues.md`) but the code itself looks finished. **Recommend**: fix the README, then link under the LangChain RAG section alongside the AWS Bedrock variant.
- **`lang-graph/tool-calling/`** — has `tool_demo.py` and `birthday_tool.py`. No README, which is why it was probably skipped. **Recommend**: write a short README and link.
- **`browser-use/find_flights.py`** — sibling of the linked `find_car_prices.py`. **Recommend**: add a second bullet under the "Browser Use" section.
- **`agents/multi-agents/park_planner_agent.py`** — single-agent variant of the linked `park_planner_multi_agent.py`. Useful as a "before / after" comparison. **Recommend**: link as a counterpart in the Multi-agents bullet, framing it as the single-agent baseline.

## Unlinked and likely intentional

- **`diffuser/residual.py`, `diffuser/sinusoidal_position_embeddings.py`** — two helper files, no README, no entry point. Tracked by issue #6 ("Work through creating a diffuser from scratch"). Leave unlinked until the example is fleshed out.
- **`agents/batch-agents/`** — tools but no entry point, empty README. Either flesh out or delete (covered in `04-readme-issues.md`).

## Linked but pointing to a directory rather than a script

The top-level README sometimes links to a directory (e.g. `[Smol Agent](/agents/smol-agent/)`) and sometimes to a specific script. This is fine when the directory README is the natural landing page, but it occasionally hides a missing README. Worth a sweep to confirm every linked directory has a useful README.

## Suggested approach

- **One sweep issue**: "Audit unlinked directories and either link or hide." The fix is mechanical once the decision is made per directory.
- For directories that need a README first (`lang-graph/tool-calling/`), each gets its own small follow-up issue.
