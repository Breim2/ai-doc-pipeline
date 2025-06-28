import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "app.log"

templates = Jinja2Templates(directory="app/web/templates")
log_router = APIRouter()

# Set up the logger with rotation
def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        # File handler with rotation
        file_handler = RotatingFileHandler(LOG_FILE, maxBytes=1_000_000, backupCount=5, encoding="utf-8")
        file_handler.setLevel(logging.INFO)
        file_format = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
        file_handler.setFormatter(file_format)

        # Console handler with safe encoding
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_format = logging.Formatter('%(message)s')
        console_handler.setFormatter(console_format)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

# Route: list all log files
@log_router.get("/logs", response_class=HTMLResponse)
async def list_logs(request: Request):
    log_files = sorted(LOG_DIR.glob("app.log*"), reverse=True)
    return templates.TemplateResponse("logs.html", {
        "request": request,
        "log_files": [f.name for f in log_files]
    })

# Route: view a specific log file
@log_router.get("/logs/{filename}", response_class=HTMLResponse)
async def read_log_file(request: Request, filename: str):
    file_path = LOG_DIR / filename
    if not file_path.exists():
        return HTMLResponse(status_code=404, content="Log file not found.")
    
    content = file_path.read_text(encoding="utf-8", errors="ignore")
    return templates.TemplateResponse("log_viewer.html", {
        "request": request,
        "filename": filename,
        "content": content.replace("\n", "<br>")
    })
