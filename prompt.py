from langchain_core.prompts import PromptTemplate

INSIGHTS_TEMPLATE = """
You are an expert resume reviewer and career advisor.
Analyze the following resume vs job description data and give actionable improvement suggestions.

DATA:
- Final Match Score: {final_score}
- Phrase Score: {phrase_score}
- Keyword Score: {keyword_score}

- Matched Skills: {matched_skills}
- Missing Skills: {missing_skills}

- Resume Keywords: {resume_keywords}
- Job Description Keywords: {jd_keywords}


TASK:
1. Provide a detailed explanation of the final match score, explaining how well the resume aligns with the job description based on the final score.
2. Highlight the key weaknesses in the resume by analyzing the matched and missing skills.
3. Suggest specific, actionable improvements to enhance the resume, especially in terms of required skills, projects, or experience.
4. Recommend important skills that the candidate should focus on learning, based on the identified gaps.
5. Offer suggestions to improve the wording, clarity, and overall impact of the resume, including use of strong action verbs and measurable achievements.
6. Conclude with a clear and concise final verdict on the candidate’s suitability for the role.

OUTPUT FORMAT:
- Score Explanation:
- Weaknesses:
- Improvements:
- Recommended Skills:
- Resume Enhancement Tips:
- Final Verdict:

RESPONSE GUIDELINES:
- Be clear, concise, and professional  
- Avoid generic advice; make suggestions specific to the provided data  
- Focus on practical and actionable recommendations  
- Do not repeat the input data unnecessarily  
"""

insights_prompt = PromptTemplate(
    input_variables=[
        "final_score",
        "phrase_score",
        "keyword_score",
        "matched_skills",
        "missing_skills",
        "resume_keywords",
        "jd_keywords"
    ],
    template=INSIGHTS_TEMPLATE
)
