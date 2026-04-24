import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from prompt import insights_prompt

# Ensure environment variables are loaded
load_dotenv()

# Optionally override if needed, otherwise ChatGroq will use the env var automatically
if not os.environ.get("GROQ_API_KEY"):
    print("Warning: GROQ_API_KEY not found in environment variables.")

def get_ai_insights(
    final_score: float, 
    phrase_score: float, 
    keyword_score: float, 
    matched_skills: set, 
    missing_skills: set, 
    resume_keywords: set, 
    jd_keywords: set
) -> str:
    """Uses Groq to generate actionable AI insights for the resume."""
    
    llm = ChatGroq(
        temperature=0.3,
        model_name="llama-3.3-70b-versatile"
    )
    
    prompt = insights_prompt.format(
        final_score=round(final_score * 100, 2),
        phrase_score=round(phrase_score * 100, 2),
        keyword_score=round(keyword_score * 100, 2),
        matched_skills=list(matched_skills),
        missing_skills=list(missing_skills),
        resume_keywords=list(resume_keywords),
        jd_keywords=list(jd_keywords)
    )
    
    try:
        response = llm.invoke(prompt)
        return response.content
    except Exception as e:
        return f"Error generating insights: {e}"
