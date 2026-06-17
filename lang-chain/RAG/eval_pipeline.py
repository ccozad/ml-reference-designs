"""Evaluation pipeline: grade a RAG answer three complementary ways.

Run index_pipeline.py first. This runs the same query through the RAG chain, then
grades the answer with three lenses that each catch a different class of issue:

  1. Code-based   - deterministic, free, catches format/structure regressions.
  2. Model-as-judge - an LLM scores relevance and faithfulness against the context.
  3. Human-grade  - the operator rates the answer 1-5 (the ground truth the other
                    two only approximate).

Output is a side-by-side JSON blob so a reader can see what eval results look like.
"""
import argparse
import json
import os
import sys

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

import rag_common as rc
from rag_pipeline import build_rag_chain, format_docs

# A good answer about task decomposition should mention these.
EXPECTED_KEYWORDS = ["task", "decomposition"]
MIN_LEN = 40
MAX_LEN = 1500


def code_based_grade(answer):
    """Deterministic checks: non-empty, length bounds, keywords, concise structure."""
    checks = {
        "non_empty": bool(answer.strip()),
        "within_length_bounds": MIN_LEN <= len(answer) <= MAX_LEN,
        "mentions_keywords": all(k.lower() in answer.lower() for k in EXPECTED_KEYWORDS),
        # The prompt asks for at most three sentences; allow a little slack.
        "at_most_three_sentences": answer.count(".") <= 4,
    }
    score = round(5 * sum(checks.values()) / len(checks), 1)
    return {"score_1_to_5": score, "checks": checks}


JUDGE_TEMPLATE = """You are grading a RAG answer. Score from 1 (poor) to 5 (excellent) on two axes:
- relevance: does the answer address the question?
- faithfulness: is the answer supported by the context, with no fabrication?

Return ONLY valid JSON of the form:
{{"relevance": <int 1-5>, "faithfulness": <int 1-5>, "reasoning": "<one sentence>"}}

Question: {question}

Context: {context}

Answer: {answer}
"""


def model_judge_grade(question, context, answer, log):
    """A separate LLM call scores relevance and faithfulness against the context."""
    llm = ChatOpenAI(model=rc.CHAT_MODEL, temperature=0)
    chain = PromptTemplate.from_template(JUDGE_TEMPLATE) | llm | StrOutputParser()
    raw = chain.invoke({"question": question, "context": context, "answer": answer})
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        log.warning("Judge did not return valid JSON: %s", raw)
        return {"relevance": None, "faithfulness": None, "reasoning": raw.strip()}


def human_grade(answer, log):
    """Prompt the operator for a 1-5 rating. Skips cleanly when non-interactive."""
    if not sys.stdin.isatty() or os.getenv("SKIP_HUMAN_EVAL"):
        log.info("Skipping human grade (non-interactive or SKIP_HUMAN_EVAL set).")
        return {"score_1_to_5": None, "note": "skipped"}
    print("\n--- Answer to grade ---\n" + answer + "\n-----------------------")
    while True:
        raw = input("Your rating (1-5, or blank to skip): ").strip()
        if not raw:
            return {"score_1_to_5": None, "note": "skipped"}
        if raw in {"1", "2", "3", "4", "5"}:
            return {"score_1_to_5": int(raw)}
        print("Please enter a number from 1 to 5.")


def parse_args():
    parser = argparse.ArgumentParser(description="Grade a RAG answer three ways: code, model-as-judge, human.")
    parser.add_argument(
        "--query",
        help=f"Question to evaluate (env QUERY; default: {rc.DEFAULT_QUERY!r})",
    )
    return parser.parse_args()


def main():
    log = rc.configure_logging()
    rc.load_environment()
    rc.require_openai_key(log)

    args = parse_args()
    query = rc.resolve(args.query, "QUERY", rc.DEFAULT_QUERY)

    log.info("Eval pipeline")
    vectorstore = rc.get_vectorstore()
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 6})
    retrieved_docs = retriever.invoke(query)
    context = format_docs(retrieved_docs)
    log.info("Retrieved %d documents", len(retrieved_docs))

    answer = build_rag_chain(retriever).invoke(query)
    log.info("Answer: %s", answer)

    results = {
        "query": query,
        "answer": answer,
        "code_based": code_based_grade(answer),
        "model_as_judge": model_judge_grade(query, context, answer, log),
        "human": human_grade(answer, log),
    }

    print("\n=== Evaluation results ===")
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
