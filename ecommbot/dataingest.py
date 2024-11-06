from langchain_astradb import AstraDBVectorStore
from dotenv import load_dotenv
import os
import pandas as pd
from ecommbot.data_converter import dataconveter  
from langchain_google_genai import GoogleGenerativeAIEmbeddings


load_dotenv()


GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY")
ASTRA_DB_API_ENDPOINT = os.getenv("ASTRA_DB_API_ENDPOINT")
ASTRA_DB_APLICATION_TOKEN = os.getenv("ASTRA_DB_APLICATION_TOKEN")
ASTRA_DB_KEYSPACE = os.getenv("ASTRA_DB_KEYSPACE")


embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001", api_key=GEMINI_API_KEY)

def ingest_data(status):
    vstore = AstraDBVectorStore(
        embedding=embedding,
        collection_name="chatbotecom",
        api_endpoint=ASTRA_DB_API_ENDPOINT,
        token=ASTRA_DB_APLICATION_TOKEN,
        namespace=ASTRA_DB_KEYSPACE
    )

    storage = status

    if storage is None:
        docs = dataconveter()  
        inserted_ids = vstore.add_documents(docs)
        return vstore, inserted_ids
    else:
        return vstore

if __name__ == '__main__':
    vstore, inserted_ids = ingest_data(None)
    print(f"\nInserted {len(inserted_ids)} documents.")
    results = vstore.similarity_search("can you tell me the low budget sound basshead?")
    
    for res in results:
        print(f"* {res.page_content} [{res.metadata}]")
