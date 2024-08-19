from azure.search.documents.indexes.models import (
    ScoringProfile,
    SearchableField,
    SearchField,
    SearchFieldDataType,
    SimpleField,
    TextWeights,
)
from langchain_community.vectorstores.azuresearch import AzureSearch

# We are using the all-MiniLM-L6-v2 model from Hugging Face
# This model has an embedding length of 384
# https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
embedding_length = 384

print("Loading Azure credentials...")
import dotenv
dotenv.load_dotenv()
vector_store_address = os.getenv("VECTOR_STORE_ADDRESS")
vector_store_key = os.getenv("VECTOR_STORE_KEY")
vector_store_name = os.get("VECTOR_STORE_NAME")
print("Credentials loaded")

fields = [
    SimpleField(
        name="id",
        type=SearchFieldDataType.String,
        key=True,
        filterable=True,
    ),
    SearchableField(
        name="content",
        type=SearchFieldDataType.String,
        searchable=True,
    ),
    SearchField(
        name="content_vector",
        type=SearchFieldDataType.Collection(SearchFieldDataType.Single),
        searchable=True,
        vector_search_dimensions=embedding_length,
    ),
    # Additional field to store the title
    SearchableField(
        name="title",
        type=SearchFieldDataType.String,
        searchable=True,
    ),
    # Additional field for filtering on document source
    SimpleField(
        name="source",
        type=SearchFieldDataType.String,
        filterable=True,
    ),
]

print("Creating Azure Search...")
vector_store = AzureSearch(
    azure_search_endpoint=vector_store_address,
    azure_search_key=vector_store_password,
    index_name=vector_store_name,
    fields=fields,
)
print("Azure Search created")