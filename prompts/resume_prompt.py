RESUME_REVIEW_PROMPT = """
You are an expert Resume Reviewer, ATS Specialist, HR Recruiter, and Career Coach.

Analyze the following resume.

Return ONLY a valid JSON object.

The JSON format should be:

{{
  "overall_score": "",
  "ats_score": "",
  "grammar_review": "",
  "formatting_review": "",
  "technical_skills": [],
  "soft_skills": [],
  "missing_skills": [],
  "missing_keywords": [],
  "professional_summary": "",
  "improved_bullet_points": [],
  "recommendations": []
}}

Resume:

{resume}
"""