import os
from google import genai

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def explain_topic(topic: str) -> str:
    prompt = f"Provide a clear, educational explanation of the following topic: {topic}"
    try:
        response = client.models.generate_content(
            model='gemini-3.8-flash',
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Error in Explanation: {e}"