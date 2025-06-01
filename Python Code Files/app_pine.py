from pinecone import Pinecone as PineconeClient, ServerlessSpec
from dotenv import load_dotenv 
import os
load_dotenv()
pinecone_api = os.getenv("PINECONE_API_KEY")
pc = PineconeClient(api_key= pinecone_api)
index_name = "quickstart"

pc.create_index(
    name=index_name,
    dimension=768, # Replace with your model dimensions
    metric="cosine", # Replace with your model metric
    spec=ServerlessSpec(
        cloud="aws",
        region="us-east-1"
    ) 
)