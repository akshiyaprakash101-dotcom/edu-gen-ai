import os
from google import genai

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def answer_question_with_gemini(question: str) -> str:
    try:
        response = client.models.generate_content(
            model='gemini-3.8-flash',
            contents=question
        )
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Error in QnA: {e}"