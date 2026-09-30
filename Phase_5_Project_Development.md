# Phase 5: Project Development Phase

## Codebase Structure
The application code is organized into a clean, modular structure:

* **`main.py`**: The entry point for the FastAPI application. Defines API endpoints (`/qa`, `/explain/`, `/summarize/`, `/quiz`, `/learn/recommendations`) and routes client requests.
* **`qna.py`**: Handles direct question-and-answer interactions using `gemini-3.8-flash`.
* **`explanation_module.py`**: Accepts educational concepts and generates clear explanations.
* **`summary_module.py`**: Formats and simplifies lengthy text passages.
* **`quiz_module.py`**: Uses custom system prompts and regex cleaning (`clean_json_block`) to force Gemini to return parseable JSON arrays containing quiz questions, options, and answers.
* **`learning_path.py`**: Generates structured, multi-tier learning roadmaps for specified topics.
* **`templates/index.html`**: Jinja2 HTML template containing form inputs and vanilla JavaScript fetch triggers.
* **`static/style.css`**: Provides styling for form layouts, input fields, and interactive quiz card results.