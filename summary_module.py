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

def summarize_text(text: str) -> str:
    api_key = get_random_key()
    if not api_key:
        return "⚠️ Error: No valid API keys found in environment variables."
        
    try:
        client = genai.Client(api_key=api_key)
        prompt = f"Summarize the following text in simple language:\n\n{text}"
        
        response = client.models.generate_content(
            model='gemini-1.5-flash',
            contents=prompt
        )
        return response.text.strip()
        
    except Exception as e:
        error_msg = str(e)
        if "429" in error_msg or "RESOURCE_EXHAUSTED" in error_msg:
            return "⚠️ Rate Limit Hit: All keys are currently busy. Please wait 30 seconds and try again."
        return f"⚠️ Error in Summary: {error_msg}"