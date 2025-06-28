from fastapi import FastAPI, UploadFile, Request, File
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from markupsafe import Markup
from pathlib import Path
import os
import shutil

from app.main import process_document
from app.utils.logger import get_logger

app = FastAPI()
logger = get_logger("interface")

# Paths
UPLOAD_FOLDER = "uploads"
LOG_FOLDER = "logs"
TEMPLATE_DIR = "app/web/templates"
STATIC_DIR = "app/web/static"
OUTPUT_DIR = "outputs"

# Create necessary directories
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(LOG_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)


# Mount static and media folders
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
app.mount("/outputs", StaticFiles(directory=OUTPUT_DIR), name="outputs")

templates = Jinja2Templates(directory=TEMPLATE_DIR)

@app.on_event("startup")
async def list_routes():
    for route in app.router.routes:
        if hasattr(route, "path"):
            print(f"[ROUTE] {route.path}")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    logger.info("Serving homepage.")
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/process/", response_class=HTMLResponse)
async def process_file(request: Request, file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    logger.info(f"Received file: {file.filename} → Saved to: {file_path}")

    summary, audio_path = process_document(file_path)

    logger.info(f"[RESULT] Summary: {summary[:100]}...")  # Preview
    logger.info(f"[RESULT] Audio saved: {audio_path}")

    return templates.TemplateResponse("index.html", {
        "request": request,
        "summary": summary,
        "audio_file": audio_path.replace("\\", "/")
    })

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    path = os.path.join(STATIC_DIR, "favicon.ico")
    if os.path.exists(path):
        return FileResponse(path)
    return HTMLResponse(status_code=404, content="Favicon not found")

@app.get("/download/{filename}")
async def download_file(filename: str):
    return FileResponse(f"{OUTPUT_DIR}/{filename}", media_type="audio/mpeg", filename=filename)

@app.get("/logs", response_class=HTMLResponse)
async def view_logs(request: Request):
    log_files = sorted(Path(LOG_FOLDER).glob("*.log*"), reverse=True)
    if not log_files:
        logger.info("No logs found when accessing /logs.")
    return templates.TemplateResponse("logs.html", {
        "request": request,
        "log_files": [f.name for f in log_files]
    })

@app.get("/logs/{filename}", response_class=HTMLResponse)
async def read_log_file(request: Request, filename: str):
    file_path = Path(LOG_FOLDER) / filename
    if not file_path.exists():
        logger.warning(f"Attempt to read missing log file: {filename}")
        return HTMLResponse(status_code=404, content="Log file not found.")

    content = file_path.read_text(encoding="utf-8", errors="ignore")
    formatted = Markup("<br>".join(content.splitlines()))

    return templates.TemplateResponse("log_viewer.html", {
        "request": request,
        "filename": filename,
        "content": formatted
    })
