import os
import random
from google import genai

def get_random_key():
    keys = [
        os.getenv("GEMINI_API_KEY_1"),
        os.getenv("GEMINI_API_KEY_2"),
        os.getenv("GEMINI_API_KEY_3")
    ]
    valid_keys = [k for k in keys if k]
    return random.choice(valid_keys) if valid_keys else None

def answer_question_with_gemini(question: str) -> str:
    api_key = get_random_key()
    if not api_key:
        return "⚠️ Error: No valid API keys found in environment variables."
        
    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model='gemini-1.5-flash',
            contents=question
        )
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Error in QnA: {e}"