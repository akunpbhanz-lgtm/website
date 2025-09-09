import os
import pickle
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer

DB_PATH = Path(__file__).resolve().parent / "chroma.pkl"


def ingest_docs(docs_path: str) -> None:
    texts: list[str] = []
    sources: list[str] = []
    for root, _, files in os.walk(docs_path):
        for fname in files:
            if fname.lower().endswith((".md", ".txt")):
                path = Path(root) / fname
                text = path.read_text(encoding="utf-8")
                texts.append(text)
                sources.append(str(path))
    vectorizer = TfidfVectorizer().fit(texts)
    matrix = vectorizer.transform(texts)
    with open(DB_PATH, "wb") as f:
        pickle.dump({"vectorizer": vectorizer, "matrix": matrix, "sources": sources, "texts": texts}, f)
