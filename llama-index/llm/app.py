from llama_index.llms.openai import OpenAI
from llama_index.core import PromptTemplate
import os
import dotenv
dotenv.load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")


llm = OpenAI(model="gpt-3.5-turbo", temperature=0)

text_qa_template = PromptTemplate(
    "Context information is below.\n"
    "---------------------\n"
    "{context_str}\n"
    "---------------------\n"
    "Given the context information and not prior knowledge, "
    "answer the question: {query_str}\n"
)

refine_template = PromptTemplate(
    "We have the opportunity to refine the original answer "
    "(only if needed) with some more context below.\n"
    "------------\n"
    "{context_msg}\n"
    "------------\n"
    "Given the new context, refine the original answer to better "
    "answer the question: {query_str}. "
    "If the context isn't useful, output the original answer again.\n"
    "Original Answer: {existing_answer}"
)

question = "What are some shape namees in geometry?"
prompt = text_qa_template.format(context_str="", query_str=question)
response = llm.complete(prompt)
print("Question: ", question)
print("Answer: ", response.text)
