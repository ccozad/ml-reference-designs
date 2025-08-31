from llama_index.core.workflow import (
    Context,
    Workflow,
    StartEvent,
    StopEvent,
    step,
)

from llama_index.llms.openai import OpenAI


from llama_index.core.schema import (
    MetadataMode,
    NodeWithScore,
    TextNode,
)

from llama_index.core.response_synthesizers import (
    ResponseMode,
    get_response_synthesizer,
)

from typing import Union, List

from events import RetrieverEvent, CreateCitationsEvent
from config import (
    CITATION_QA_TEMPLATE,
    CITATION_REFINE_TEMPLATE
)

class CitationQueryEngineWorkflow(Workflow):
    @step
    async def retrieve(
        self, ctx: Context, ev: StartEvent
    ) -> Union[RetrieverEvent, None]:
        "Entry point for RAG, triggered by a StartEvent with `query`."
        query = ev.get("query")
        if not query:
            return None

        print(f"\nQuery the database with: {query}")

        # store the query in the global context
        await ctx.store.set("query", query)

        if ev.index is None:
            print("Index is empty, load some documents before querying!")
            return None

        retriever = ev.index.as_retriever(similarity_top_k=3)
        nodes = retriever.retrieve(query)
        print(f"\nRetrieved {len(nodes)} nodes.")
        return RetrieverEvent(nodes=nodes)

    @step
    async def create_citation_nodes(
        self, ev: RetrieverEvent
    ) -> CreateCitationsEvent:
        """
        Modify retrieved nodes to create granular sources for citations.

        Takes a list of NodeWithScore objects and adds a source number to each node.

        Args:
            nodes (List[NodeWithScore]): A list of NodeWithScore objects to be processed.

        Returns:
            List[NodeWithScore]: A new list of NodeWithScore objects labeled as a source.
        """
        nodes = ev.nodes

        new_nodes: List[NodeWithScore] = []


        for node in nodes:
            text = f"Source {len(new_nodes)+1}:\n{node.node.text}\n"
            new_text_node = TextNode(
                text=text,
                id_=node.node.id_,
                metadata=node.node.metadata,
            )
            new_node = NodeWithScore(
                node=new_text_node, score=node.score
            )

            new_nodes.append(new_node)
        
        return CreateCitationsEvent(nodes=new_nodes)

    @step
    async def synthesize(
        self, ctx: Context, ev: CreateCitationsEvent
    ) -> StopEvent:
        """Return a streaming response using the retrieved nodes."""
        llm = OpenAI(model="gpt-4o-mini")
        query = await ctx.store.get("query", default=None)

        synthesizer = get_response_synthesizer(
            llm=llm,
            text_qa_template=CITATION_QA_TEMPLATE,
            refine_template=CITATION_REFINE_TEMPLATE,
            response_mode="compact",
            use_async=True,
        )

        response = await synthesizer.asynthesize(query, nodes=ev.nodes)
        return StopEvent(result=response)