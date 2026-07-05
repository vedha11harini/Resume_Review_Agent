import json

from config.llm import llm
from prompts.resume_prompt import RESUME_REVIEW_PROMPT

from tools.skill_tool import extract_skills
from tools.bullet_tool import improve_bullets


def analyze_resume(resume_text):
    """
    Main Resume Review Agent

    Workflow:
    1. Creates prompt
    2. Sends prompt to Gemini
    3. Receives JSON response
    4. Processes skills
    5. Processes bullet points
    6. Returns final structured report
    """

    # Create Prompt
    prompt = RESUME_REVIEW_PROMPT.format(
        resume=resume_text
    )

    # Call Gemini
    response = llm.invoke(prompt)

    result = response.content

    # Remove markdown if Gemini returns
    # ```json ... ```
    result = result.replace("```json", "")
    result = result.replace("```", "")
    result = result.strip()

    try:

        analysis = json.loads(result)

        # -----------------------------
        # Skill Processing
        # -----------------------------
        skills = extract_skills(analysis)

        analysis["technical_skills"] = skills["technical_skills"]
        analysis["soft_skills"] = skills["soft_skills"]
        analysis["missing_skills"] = skills["missing_skills"]
        analysis["missing_keywords"] = skills["missing_keywords"]

        # -----------------------------
        # Improved Bullet Points
        # -----------------------------
        analysis["improved_bullet_points"] = improve_bullets(analysis)

        return analysis

    except Exception:

        return {
            "error": result
        }