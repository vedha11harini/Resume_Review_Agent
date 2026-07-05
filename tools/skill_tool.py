def extract_skills(analysis):
    """
    Extract skills information from Gemini response.
    """

    return {
        "technical_skills": analysis.get("technical_skills", []),
        "soft_skills": analysis.get("soft_skills", []),
        "missing_skills": analysis.get("missing_skills", []),
        "missing_keywords": analysis.get("missing_keywords", [])
    }