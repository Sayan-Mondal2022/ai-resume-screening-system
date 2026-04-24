import streamlit as st
import tempfile
import os

from parser import save_uploaded_file, load_text, clean_text
from extractor import extract_data
from embedder import batch_encode
from scorer import get_phrase_score, get_keyword_score, get_final_score
from ai_insights import get_ai_insights

st.set_page_config(page_title="AI Resume Screening System", layout="wide")

st.title("AI Resume Screening & JD Matching")
st.markdown("Analyze resumes against job descriptions using NLP, sentence embeddings, and AI Insights.")

col1, col2 = st.columns(2)

with col1:
    st.header("Resume")
    resume_option = st.radio("Input Method for Resume", ["Paste Text", "Upload File"], key="resume_opt")
    resume_text_input = ""
    resume_file = None
    
    if resume_option == "Paste Text":
        resume_text_input = st.text_area("Paste Resume Text Here", height=300)
    else:
        resume_file = st.file_uploader("Upload Resume (PDF or TXT)", type=["pdf", "txt"], key="resume_file")

with col2:
    st.header("Job Description (JD)")
    jd_option = st.radio("Input Method for JD", ["Paste Text", "Upload File"], key="jd_opt")
    jd_text_input = ""
    jd_file = None
    
    if jd_option == "Paste Text":
        jd_text_input = st.text_area("Paste JD Text Here", height=300)
    else:
        jd_file = st.file_uploader("Upload JD (PDF or TXT)", type=["pdf", "txt"], key="jd_file")

if st.button("Analyze", type="primary", use_container_width=True):
    with st.spinner("Processing documents..."):
        # Process Resume
        resume_text = ""
        if resume_option == "Paste Text":
            resume_text = resume_text_input
        elif resume_file is not None:
            temp_path = save_uploaded_file(resume_file)
            resume_text = load_text(temp_path)
            os.remove(temp_path)
            
        # Process JD
        jd_text = ""
        if jd_option == "Paste Text":
            jd_text = jd_text_input
        elif jd_file is not None:
            temp_path = save_uploaded_file(jd_file)
            jd_text = load_text(temp_path)
            os.remove(temp_path)

        # Validation
        if not resume_text.strip():
            st.error("Please provide Resume content.")
            st.stop()
        if not jd_text.strip():
            st.error("Please provide Job Description content.")
            st.stop()

        # Pipeline Execution
        try:
            # Clean and Extract
            st.toast("Extracting keywords and phrases...")
            resume_text_clean = clean_text(resume_text)
            jd_text_clean = clean_text(jd_text)
            
            resume_data = extract_data(resume_text_clean)
            jd_data = extract_data(jd_text_clean)
            
            # Embeddings
            st.toast("Generating embeddings...")
            resume_embeddings = batch_encode(resume_data["phrases"])
            jd_embeddings = batch_encode(jd_data["phrases"])
            
            # Scoring
            st.toast("Calculating similarity scores...")
            phrase_score = get_phrase_score(resume_embeddings, jd_embeddings)
            
            keyword_results = get_keyword_score(resume_data["keywords"], jd_data["keywords"])
            keyword_score = keyword_results["keyword_score"]
            matched_skills = keyword_results["matched_skills"]
            missing_skills = keyword_results["missing_skills"]
            
            final_score = get_final_score(phrase_score, keyword_score)
            
            # Output Display
            st.divider()
            st.header("Analysis Results")
            
            # Display Scores
            score_col1, score_col2, score_col3 = st.columns(3)
            with score_col1:
                st.metric(label="Final Score", value=f"{final_score * 100:.2f}%")
            with score_col2:
                st.metric(label="Keyword Match Score", value=f"{keyword_score * 100:.2f}%")
            with score_col3:
                st.metric(label="Phrase Similarity Score", value=f"{phrase_score * 100:.2f}%")
            
            # Generate and Display AI Insights
            st.toast("Generating AI Insights...")
            with st.spinner("Generating detailed feedback..."):
                insights = get_ai_insights(
                    final_score=final_score,
                    phrase_score=phrase_score,
                    keyword_score=keyword_score,
                    matched_skills=matched_skills,
                    missing_skills=missing_skills,
                    resume_keywords=resume_data["keywords"],
                    jd_keywords=jd_data["keywords"]
                )
            
            st.subheader("AI Insights & Recommendations")
            st.markdown(insights)
            
            # Show additional details in an expander
            with st.expander("View Raw Keyword Data"):
                st.write("**Matched Skills:**")
                st.write(", ".join(matched_skills) if matched_skills else "None")
                st.write("**Missing Skills:**")
                st.write(", ".join(missing_skills) if missing_skills else "None")

        except Exception as e:
            st.error(f"An error occurred during analysis: {e}")
