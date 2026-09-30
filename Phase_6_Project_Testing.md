# Phase 6: Project Testing Phase

## Test Cases & Resolution Log

| Test Case / Issue | Description | Cause | Resolution |
|---|---|---|---|
| **API Authentication Failure** | `401 Unauthorized` / `404 Not Found` when calling Gemini API | Deprecated SDK syntax (`google.generativeai`) and improper model naming | Upgraded to the modern `google-genai` Python SDK and standardized model calls to `gemini-3.8-flash` |
| **API Key Exposure Risk** | Hardcoded API keys inside source files | Public Git exposure risks | Refactored all modules to load keys dynamically via `os.getenv("GEMINI_API_KEY")` |
| **Quiz JSON Parsing Error** | HTML output displaying raw markdown code blocks (` ```json ... ``` `) | Model wrapping JSON in markdown blocks | Created a regex helper function (`clean_json_block`) to strip markdown fences before JSON parsing |
| **Deployment Server Crash** | Render deployment failing with `ImportError: cannot import name 'genai' from 'google'` | Heavy local ML dependencies (`torch`, `transformers`) and missing `google-genai` in deployment environment | Sanitized `requirements.txt` down to essential web dependencies (`fastapi`, `uvicorn`, `jinja2`, `google-genai`) |