GRAMMAR_PROMPT = """
You are an expert English grammar reviewer and professional resume writer.

Analyze the following resume.

Resume:
{resume}

Instructions:

1. Find grammar mistakes.
2. Find spelling mistakes.
3. Improve sentence clarity.
4. Suggest professional wording.
5. Do NOT rewrite the whole resume.
6. Return the answer in this format:

Grammar Score: xx/100

Grammar Mistakes:
- ...

Spelling Mistakes:
- ...

Suggestions:
- ...

Professional Writing Tips:
- ...
"""