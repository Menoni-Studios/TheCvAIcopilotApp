from fastapi import FastAPI, UploadFile, File, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.requests import Request

from services.cv_parser import extract_text
from services.job_analyzer import analyze_match

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.post("/analyze")
async def analyze(
    job_description: str = Form(...),
    cv_file: UploadFile = File(...)
):

    cv_text = await extract_text(cv_file)

    result = analyze_match(
        cv_text,
        job_description
    )

    return result