# AI Resume Screening & JD Matching System

An intelligent application designed to automate and enhance the resume screening process by comparing candidate resumes against job descriptions (JDs). It uses natural language processing and advanced AI to provide an accurate compatibility score and actionable feedback.

## Project Overview
This project evaluates the fit between a candidate's resume and a job description. It employs a multi-layered approach: extracting keywords and phrases using **spaCy**, generating semantic embeddings via **SentenceTransformers**, and computing similarity scores. Finally, it integrates with **Groq's Llama 3** model through **LangChain** to generate detailed AI insights, highlighting strengths, missing skills, and concrete recommendations for the candidate. **Langsmith** is used for tracing and monitoring the Langchain runs.

The architecture is fully modularized, cleanly separating concerns across document parsing, keyword extraction, embedding generation, scoring, and UI rendering.

## Demo Link
[Click Here](https://ai-resume-screening-system-01.streamlit.app)

## Tech Stack
* **Language**: Python 3.11
* **Frontend/UI**: Streamlit
* **NLP & Text Processing**: spaCy (`en_core_web_sm`)
* **Embeddings**: SentenceTransformers (`all-MiniLM-L6-v2`)
* **Document Parsing**: PDFPlumber
* **LLM Orchestration**: LangChain
* **LLM Provider**: Groq API (Llama 3.3 70B Versatile)
* **Machine Learning**: scikit-learn, NumPy
* **Langsmith**: For tracing and monitoring the Langchain runs

## Key Features
* **Multi-Format Input Support**: Upload resumes and JDs as PDFs or TXT files, or paste raw text directly.
* **Semantic Phrase Matching**: Uses state-of-the-art sentence embeddings to understand the context of experience beyond exact keyword matching.
* **Keyword Analysis**: Accurately extracts and compares critical skills and nouns to identify missing core competencies.
* **Comprehensive Scoring**: Provides a weighted final score derived from phrase similarity and keyword matches.
* **Actionable AI Insights**: Leverages Groq's LLM to provide a detailed breakdown of the candidate's strengths, weaknesses, and specific steps for resume enhancement.
* **Clean, Interactive UI**: Built with Streamlit for a responsive, two-column comparative experience.
* **Langsmith Tracing**: Traces and monitors the Langchain runs to identify issues and debug.

## Installation and Setup Instructions

Follow these steps to run the project locally on your machine:

### 1. Clone the Repository
```bash
git clone https://github.com/Sayan-Mondal2022/ai-resume-screening-system.git
cd ai-resume-screening-system
```

### 2. Create a Virtual Environment
Ensure you are using **Python 3.11**.
```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
*(Note: The requirements file is configured to install the necessary packages. If the spaCy model does not download automatically, run `python -m spacy download en_core_web_sm` manually).*

### 4. Set Up Environment Variables
Create a `.env` file in the root directory of the project and add your Groq API key:
```env
GROQ_API_KEY=YOUR_API_KEY
```

And if you want tracing then add the following as well

```env
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
LANGSMITH_API_KEY=<YOUR_API_KEY>
LANGSMITH_PROJECT="YOU_PROJECT_NAME"
```

### 5. Run the Application
```bash
streamlit run app.py
```
This will launch the Streamlit server. You can view the application in your browser at the provided local URL (usually `http://localhost:8501`).

## Future Enhancements
* **Batch Processing**: Allow HR professionals to upload multiple resumes against a single JD and rank them automatically.
* **Extended Document Support**: Add support for `.docx` and image-based PDFs (using OCR).
* **Customizable Scoring Weights**: Let the user adjust the 70/30 weighting between phrase similarity and keyword matching via the Streamlit UI.
* **Export Functionality**: Allow users to download the AI-generated insights as a PDF report.

## Acknowledgements
This project is built upon several incredible open-source tools and libraries:
* [spaCy](https://spacy.io/usage) - Industrial-strength Natural Language Processing in Python.
* [Groq](https://console.groq.com/docs/quickstart) - Fast AI inference and Llama 3 models.
* [PDFPlumber](https://github.com/jsvine/pdfplumber#readme) - Plumb a PDF for detailed text extraction.
* [LangChain](https://python.langchain.com/docs/get_started/introduction) - Framework for developing applications powered by language models.
* [Streamlit](https://docs.streamlit.io/) - The fastest way to build and share data apps.
* [Langsmith](https://docs.smith.langchain.com/) - The fastest way to build and share data apps.

## Thank You!
Thank you for taking the time to view this project! Your interest and time are highly appreciated. 

## Open for Collaboration
I am always open to feedback, suggestions, and contributions! Feel free to open an issue or submit a pull request if you have ideas on how to improve this system. If you'd like to connect or collaborate on future AI/ML projects, don't hesitate to reach out!
