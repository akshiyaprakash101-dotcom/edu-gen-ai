import os
import re
from google import genai

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def clean_json_block(text):
    return re.sub(r"```(?:json)?\n(.*?)```", r"\1", text, flags=re.DOTALL).strip()

def generate_quiz(text: str) -> list:
    try:
        prompt = f"""
You are a quiz generator.
From the following passage, create 3 multiple-choice questions. Each question should include:
- A "question"
- A list of 4 "options"
- A correct "answer" that must exactly match one of the options.

Format your output as **valid JSON**, like this:
[
  {{
    "question": "What is ...?",
    "options": ["A", "B", "C", "D"],
    "answer": "A"
  }}
]

Passage:
{text}
"""
        response = client.models.generate_content(
            model='gemini-3.8-flash',
            contents=prompt
        )
        quiz_text = response.text.strip()
        cleaned_text = clean_json_block(quiz_text)
        return cleaned_text
    except Exception as e:
        return f"⚠️ Error in Quiz: {e}"