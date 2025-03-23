import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.PersistentClient("data/chromadb")
collection = client.get_collection("subtitles")

def search_subtitles(query):
    query_embedding = model.encode(query).tolist()
    results = collection.query(query_embeddings=[query_embedding], n_results=5)
    return results["documents"][0]

query = "Where is the treasure hidden?"
print("Search Results:", search_subtitles(query))