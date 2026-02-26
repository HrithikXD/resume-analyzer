Resume Analyzer

Resume Analyzer is a lightweight FastAPI service that extracts text from PDF resumes and uses an LLM to generate an objective score and actionable feedback for candidates and recruiters.

## What it does

- Accepts PDF resume uploads via a `/analyze` endpoint
- Extracts text from PDFs using `pypdf`
- Sends the extracted text to the Groq LLM to produce:
  - A score (out of 100)
  - 5 strengths
  - 5 weaknesses
  - 5 improvement suggestions
- Returns structured JSON suitable for UI integration or automation

## Tech stack

- Python
- FastAPI
- pypdf
- Groq API (LLM)

## Prerequisites

- Python 3.10+
- Git (optional)
- A Groq API key (set as `GROQ_KEY` environment variable)

## Local setup (Windows PowerShell)

1. Clone the repo (if needed) and change to the project directory:

```powershell
git clone <repo-url>
cd resume-analyzer
```

2. Create and activate a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
pip install -r requirements.txt
```

4. Set your Groq API key (temporary for current session):

```powershell
$env:GROQ_KEY = 'your_groq_api_key_here'
```

## Local setup (macOS / Linux)

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export GROQ_KEY='your_groq_api_key_here'
```

## Run the app

Start the FastAPI app with Uvicorn:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API docs are available at `http://localhost:8000/docs`.

## Example API request (curl)

```bash
curl -X POST "http://localhost:8000/analyze" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "file=@/path/to/resume.pdf;type=application/pdf"
```

## Files to know

- `main.py` - FastAPI app and `/analyze` endpoint
- `utils/resume_parser.py` - PDF text extraction
- `services/llm.py` - Groq LLM integration and analysis prompt

## Notes

- Set `GROQ_KEY` to a valid API key before running.
- For production, secure environment variables and consider containerization.

Enjoy — ask if you want a Dockerfile or a simple frontend demo.
