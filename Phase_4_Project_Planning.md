# Phase 4: Project Planning Phase

## Development Roadmap
The project was executed in a structured, phase-wise approach to ensure stability before integrating the cloud AI layers.

* **Step 1: Environment Setup & Foundation**
  * Initialize the virtual environment and install core requirements (`fastapi`, `uvicorn`, `jinja2`).
  * Set up the base directory structure (`templates/`, `static/`, and root modules).

* **Step 2: API Integration & Security**
  * Migrate from the legacy generative AI library to the modern `google-genai` SDK to support the new "AQ" API key format.
  * Implement environment variables (`os.getenv`) to ensure the `GEMINI_API_KEY` is never hardcoded in the public repository.

* **Step 3: Backend Module Development**
  * Construct individual Python files for each AI function.
  * Engineer strict prompts, particularly for the `quiz_module.py` to ensure it consistently returns parseable JSON data.
  * Wire the FastAPI routing in `main.py` to connect to these modules.

* **Step 4: Frontend Development & Interactivity**
  * Build `index.html` with form structures.
  * Write vanilla JavaScript to capture form submissions, send asynchronous requests to the FastAPI backend, and render the responses.
  * Implement logic to parse JSON quiz data into clickable HTML radio buttons with live answer validation.

* **Step 5: Cloud Deployment**
  * Create a sanitized `requirements.txt` strictly containing necessary web dependencies (omitting heavy local machine learning libraries).
  * Push the secure repository to GitHub.
  * Connect the repository to Render.com for continuous deployment and set server-side environment variables.