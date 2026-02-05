import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_KEY"))

def analyze_resume(resume_text: str):
    prompt = f"""
You are a professional technical recruiter.

Analyze the following resume and return:
1. Score out of 100
2. 5 Strengths
3. 5 Weaknesses
4. 5 Suggestions for improvement

Resume:
{resume_text}
"""
    response = client.chat.completions.create(
        model = "llama-3.3-70b-versatile",
        messages=[
            {"role":"system", "content":"You are a helpful recruiter."},
            {"role":"user", "content":prompt}
        ],
        temperature=0.3,
        max_tokens=800
    )
    return {
        "analysis" : response.choices[0].message.content
    }