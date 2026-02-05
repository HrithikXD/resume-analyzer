from fastapi import FastAPI, UploadFile, File, HTTPException
from utils.resume_parser import extract_text_from_pdf
from services.llm import analyze_resume

app = FastAPI(title="Resume Analyzer")
@app.post("/analyze")

async def analyze(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Please upload PDF")
    content = await file.read()
    text = extract_text_from_pdf(content)
    result = analyze_resume(text)
    return result
