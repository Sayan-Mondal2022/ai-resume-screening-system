import numpy as np
from numpy import ndarray
from sklearn.metrics.pairwise import cosine_similarity

def get_phrase_score(resume_embeddings: list[ndarray], jd_embeddings: list[ndarray]) -> float:
    """Computes the cosine similarity between resume and JD phrase embeddings."""
    if len(resume_embeddings) == 0 or len(jd_embeddings) == 0:
        return 0.0

    score_matrix = cosine_similarity(
        resume_embeddings, jd_embeddings
    )

    best_matches = np.max(score_matrix, axis=1)

    return float(best_matches.mean())

def get_keyword_score(resume_keywords: set[str], jd_keywords: set[str]) -> dict:
    """Computes keyword match statistics and score."""
    if not jd_keywords:
        return {
            "matched_skills": set(),
            "missing_skills": set(),
            "keyword_score": 0.0
        }

    matched_skills = resume_keywords & jd_keywords
    missing_skills = jd_keywords - resume_keywords

    keyword_score = len(matched_skills) / len(jd_keywords)

    return {
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "keyword_score": keyword_score
    }

def get_final_score(phrase_score: float, keyword_score: float) -> float:
    """Calculates the weighted final score."""
    return (0.7 * phrase_score) + (0.3 * keyword_score)
