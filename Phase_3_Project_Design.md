# Phase 3: Project Design Phase

## Architectural Design
EduGenie uses a streamlined, modular web architecture designed for fast deployment and clear separation of concerns. 
* **Client Side:** A single-page HTML interface structured with Jinja2 templating and styled with modern CSS. Asynchronous JavaScript `fetch()` calls handle interactions without requiring page reloads.
* **Server Side:** A FastAPI application (`main.py`) acts as the central router, directing HTTP requests to dedicated Python modules.
* **AI Processing Layer:** Specialized Python helper files interface securely with the Google Gemini API to process prompts and format specific outputs (e.g., forcing JSON generation for quizzes).

## Modular Code Structure
The backend logic is intentionally decoupled into specific task modules to maintain clean code and easy debugging:
* `qna.py` -> Handles general knowledge queries.
* `explanation_module.py` -> Processes complex topics into educational breakdowns.
* `summary_module.py` -> Condenses large text inputs.
* `quiz_module.py` -> Generates structured JSON for multiple-choice quizzes.
* `learning_path.py` -> Maps out structured educational journeys.

## User Interface (UI) Design
The frontend uses a clean, minimalist aesthetic optimized for accessibility and focus:
* **Layout:** Centered max-width container with distinct, visually separated sections for each tool (Q&A, Explanation, Summary, Quiz).
* **Styling:** Soft gray background (`#f8f9fb`), rounded input fields, and distinct blue primary action buttons (`#4285f4`) to indicate interactivity.
* **Feedback:** Dynamic DOM updates provide immediate visual feedback (e.g., displaying "Thinking..." during API calls and rendering color-coded feedback for correct/incorrect quiz answers).