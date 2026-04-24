import spacy

try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("Downloading spacy en_core_web_sm model...")
    from spacy.cli import download
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

def extract_data(text: str) -> dict:
    """Extracts keywords and phrases from the given text using Spacy."""
    doc = nlp(text)

    keywords = set()
    phrases = []

    for token in doc:
        if token.pos_ in ["NOUN", "PROPN", "ADJ"]:
            keywords.add(token.lemma_.lower())

    phrases = [
        chunk.text.lower() for chunk in doc.noun_chunks if len(chunk.text.split()) > 1
    ]

    phrases = list(filter(lambda phrase: phrase not in keywords, phrases))

    return {"phrases": phrases, "keywords": keywords}
