from langchain.docstore.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from smolagents import Tool
from langchain_community.retrievers import BM25Retriever
from smolagents import CodeAgent, HfApiModel

class NistCyberSecurityFrameworkRetrieverTool(Tool):
    name = "nist_cybersecurity_retriever"
    description = "Uses semantic search to retrieve relevant NIST Cyber Security Framework practices based on a query."
    inputs = {
        "query": {
            "type": "string",
            "description": "The query to perform. This should be a query related to cybersecurity",
        }
    }
    output_type = "string"

    def __init__(self, docs, **kwargs):
        super().__init__(**kwargs)
        self.retriever = BM25Retriever.from_documents(
            docs, k=5  # Retrieve the top 5 documents
        )

    def forward(self, query: str) -> str:
        assert isinstance(query, str), "Your search query must be a string"

        docs = self.retriever.invoke(
            query,
        )
        return "\nRetrieved practices:\n" + "".join(
            [
                f"\n\n===== Practice {str(i)} =====\n" + doc.page_content
                for i, doc in enumerate(docs)
            ]
        )

# Hard code the NIST Cyber Security Governance practices
security_practices = [
    {"text": "The organization’s cybersecurity risk management strategy, expectations, and policy are established, communicated, and monitored", "source": "GOVERN (GV)"},
    {"text": "The circumstances — mission, stakeholder expectations, dependencies, and legal, regulatory, and contractual requirements — surrounding the organization’s cybersecurity risk management decisions are understood", "source": "Organizational Context (GV.OC)"},
    {"text": "The organizational mission is understood and informs cybersecurity risk management", "source": "GV.OC-01"},
    {"text": "Internal and external stakeholders are understood, and their needs and expectations regarding cybersecurity risk management are understood and considered", "source": "GV.OC-02"},
    {"text": "Legal, regulatory, and contractual requirements regarding cybersecurity — including privacy and civil liberties obligations — are understood and managed", "source": "GV.OC-03"},
    {"text": "Critical objectives, capabilities, and services that external stakeholders depend on or expect from the organization are understood and communicated", "source": "GV.OC-04"},
    {"text": "Outcomes, capabilities, and services that the organization depends on are understood and communicated", "source": "GV.OC-05"},
    {"text": "The organization’s priorities, constraints, risk tolerance and appetite statements, and assumptions are established, communicated, and used to support operational risk decisions", "source": "Risk Management Strategy (GV.RM)"},
    {"text": "Risk management objectives are established and agreed to by organizational stakeholders", "source": "GV.RM-01"},
    {"text": "Risk appetite and risk tolerance statements are established, communicated, and maintained", "source": "GV.RM-02"},
    {"text": "Cybersecurity risk management activities and outcomes are included in enterprise risk management processes", "source": "GV.RM-03"},
    {"text": "Strategic direction that describes appropriate risk response options is established and communicated", "source": "GV.RM-04"},
    {"text": "Lines of communication across the organization are established for cybersecurity risks, including risks from suppliers and other third parties", "source": "GV.RM-05"},
    {"text": "A standardized method for calculating, documenting, categorizing, and prioritizing cybersecurity risks is established and communicated", "source": "GV.RM-06"},
    {"text": "Strategic opportunities (i.e., positive risks) are characterized and are included in organizational cybersecurity risk discussions", "source": "GV.RM-07"},
]

source_docs = [
    Document(page_content=doc["text"], metadata={"source": doc["source"]})
    for doc in security_practices
]

# Split the documents into smaller chunks for more efficient search
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
    add_start_index=True,
    strip_whitespace=True,
    separators=["\n\n", "\n", ".", " ", ""],
)
docs_processed = text_splitter.split_documents(source_docs)

# Create the retriever tool
nist_csf_retriever = NistCyberSecurityFrameworkRetrieverTool(docs_processed)

# Initialize the agent
agent = CodeAgent(tools=[nist_csf_retriever], model=HfApiModel())

# Example usage
response = agent.run(
    "List security practices related to commuinication in the organization. Use only information from the NIST Cyber Security Framework. If you don't have the information, please say you don't know."
)

print(response)