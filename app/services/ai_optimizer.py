from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def optimize_cv(cv_text, job_text):

    prompt = f"""
    Improve this CV for the role.

    CV:

    {cv_text}

    Job:

    {job_text}

    Do not invent skills,
    certifications or experience.

    Return improved CV text.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return response.choices[0].message.content