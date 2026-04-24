import os
import re
import tempfile
from langchain_community.document_loaders import PDFPlumberLoader, TextLoader

def save_uploaded_file(uploaded_file):
    """Saves a Streamlit UploadedFile to a temporary local file and returns the path."""
    if uploaded_file is None:
        return None
    # Extract suffix to maintain file type
    suffix = os.path.splitext(uploaded_file.name)[1]
    # Create a temporary file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
    temp_file.write(uploaded_file.getvalue())
    temp_file.close()
    return temp_file.name

def load_text(file_path: str) -> str:
    """Loads text from a PDF or TXT file."""
    if file_path.endswith(".pdf"):
        loader = PDFPlumberLoader(file_path)
    elif file_path.endswith(".txt"):
        loader = TextLoader(file_path, encoding="utf-8")
    else:
        raise ValueError(f"Unsupported file type: {file_path}")

    documents = loader.load()
    if not documents:
        return ""

    text = "\n".join([doc.page_content.strip() for doc in documents if doc.page_content])
    return text

def clean_text(text: str) -> str:
    """Cleans the extracted text."""
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s\.:/\-]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()
