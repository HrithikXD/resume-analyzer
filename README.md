A lightweight FastAPI service that extracts text from PDF resumes and uses an LLM to generate an objective score and actionable feedback for candidates and recruiters.

What I built:
Designed a main.py endpoint to accept PDF uploads and return analysis.
Implemented PDF text extraction with pypdf.
Integrated the Groq LLM (Llama 3.3) to produce: a score (out of 100), 5 strengths, 5 weaknesses, and 5 improvement suggestions.
Returned structured JSON for easy integration with UIs or pipelines.
Tech stack: Python, FastAPI, pypdf, Groq API (Llama 3.3), Docker (optional)

To run the app install requrements.text modules.
add your api key in llm.py.
now you are good to go, call the api using swagger/postmen etc.
