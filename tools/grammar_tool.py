from config.llm import llm
from prompts.prompts import GRAMMAR_PROMPT


def grammar_review(resume_text):

    prompt = GRAMMAR_PROMPT.format(
        resume=resume_text
    )

    response = llm.invoke(prompt)

    return response.content