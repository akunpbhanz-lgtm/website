import pickle
from pathlib import Path
from sklearn.metrics.pairwise import cosine_similarity
from .ingest import DB_PATH


def query_docs(query: str) -> str:
    if not DB_PATH.exists():
        return "No knowledge base. Please run ingest first."
    data = pickle.loads(DB_PATH.read_bytes())
    vectorizer = data["vectorizer"]
    matrix = data["matrix"]
    texts = data["texts"]
    sources = data["sources"]
    q_vec = vectorizer.transform([query])
    sims = cosine_similarity(q_vec, matrix)[0]
    idx = sims.argmax()
    snippet = texts[idx][:200].replace("\n", " ")
    src = sources[idx]
    return f"{snippet} ({src})"
