from sentence_transformers import SentenceTransformer
import pandas as pd
import chromadb

model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.PersistentClient("data/chromadb")
collection = client.get_or_create_collection("subtitles")

def generate_embeddings():
    df = pd.read_csv("data/cleaned_subtitles.csv")
    for idx, row in df.iterrows():
        embedding = model.encode(row["Content"]).tolist()
        collection.add(ids=[str(row["ID"])], embeddings=[embedding], metadatas=[{"file": row["File Name"]}])
    print("Embeddings stored in ChromaDB!")

generate_embeddings()