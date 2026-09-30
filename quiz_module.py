import os
import re
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

def clean_json_block(text):
    return re.sub(r"```(?:json)?\n(.*?)```", r"\1", text, flags=re.DOTALL).strip()

def generate_quiz(text: str) -> list:
    api_key = get_random_key()
    if not api_key:
        return '[{"question": "⚠️ Error: No API keys configured.", "options": ["OK"], "answer": "OK"}]'

    try:
        client = genai.Client(api_key=api_key)
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
            model='gemini-1.5-flash',
            contents=prompt
        )
        quiz_text = response.text.strip()
        cleaned_text = clean_json_block(quiz_text)
        return cleaned_text
    except Exception as e:
        error_msg = str(e)
        if "429" in error_msg or "RESOURCE_EXHAUSTED" in error_msg:
            return '[{"question": "⚠️ Rate Limit Hit: All keys are currently exhausted. Please wait 30 seconds.", "options": ["Will do"], "answer": "Will do"}]'
        return f'[{"question": "⚠️ Error generating quiz.", "options": ["1", "2", "3", "4"], "answer": "1"}]'