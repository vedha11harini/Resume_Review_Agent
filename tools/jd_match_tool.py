def match_resume_with_jd(analysis, job_description):
    """
    Compare resume with job description.
    """

    resume_skills = set(
        skill.lower()
        for skill in analysis.get("technical_skills", [])
    )

    jd_words = set(job_description.lower().split())

    matched = []

    missing = []

    for word in jd_words:

        if word in resume_skills:
            matched.append(word)

        else:
            missing.append(word)

    score = round(
        (len(matched) / max(len(jd_words), 1)) * 100,
        2
    )

    return {
        "match_score": score,
        "matched_skills": matched,
        "missing_skills": missing
    }