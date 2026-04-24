from sentence_transformers import SentenceTransformer

# Initialize the model once
model = SentenceTransformer('all-MiniLM-L6-v2')

def batch_encode(text_list: list[str]):
    """Encodes a list of text strings into embeddings using sentence-transformers."""
    if not text_list:
        return []
    return model.encode(text_list)
