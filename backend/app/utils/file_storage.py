from pathlib import Path
from fastapi import UploadFile

BASE_DIR = Path(__file__).resolve().parent.parent.parent
UPLOAD_DIR = BASE_DIR / "data" / "uploads"
PROCESSED_DIR = BASE_DIR / "data" / "processed"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

LATEST_CLEANED_PATH = PROCESSED_DIR / "latest_cleaned_city_day.csv"

def safe_filename(name: str) -> str:
    return Path(name).name.replace(" ", "_")

async def save_upload(file: UploadFile) -> Path:
    filename = safe_filename(file.filename or "upload.csv")
    path = UPLOAD_DIR / filename
    content = await file.read()
    path.write_bytes(content)
    return path

def latest_cleaned_path() -> Path:
    return LATEST_CLEANED_PATH
