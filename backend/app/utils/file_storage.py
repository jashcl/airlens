"""Storage paths and file-writing helpers for uploaded datasets."""

from pathlib import Path

import pandas as pd


BACKEND_DIRECTORY = Path(__file__).resolve().parents[2]
UPLOAD_DIRECTORY = BACKEND_DIRECTORY / "data" / "uploads"
PROCESSED_DIRECTORY = BACKEND_DIRECTORY / "data" / "processed"
CLEANED_CITY_DAY_PATH = PROCESSED_DIRECTORY / "latest_cleaned_city_day.csv"


def validate_csv_filename(filename: str | None) -> str:
    """Validate and safely reduce an uploaded name to its filename."""
    if not filename:
        raise ValueError("A CSV filename is required.")

    safe_filename = Path(filename).name
    if Path(safe_filename).suffix.lower() != ".csv":
        raise ValueError("Only CSV files are supported. Please upload a .csv file.")

    return safe_filename


def validate_upload_content(content: bytes) -> None:
    """Require upload content before CSV parsing and persistence."""
    if not content:
        raise ValueError("The uploaded CSV file is empty.")


def save_uploaded_file(filename: str, content: bytes) -> Path:
    """Save a validated uploaded CSV source file in the uploads directory."""
    UPLOAD_DIRECTORY.mkdir(parents=True, exist_ok=True)
    destination = UPLOAD_DIRECTORY / filename
    destination.write_bytes(content)
    return destination


def save_cleaned_dataset(dataframe: pd.DataFrame) -> Path:
    """Write the latest cleaned city-day dataset for downstream analysis."""
    PROCESSED_DIRECTORY.mkdir(parents=True, exist_ok=True)
    dataframe.to_csv(CLEANED_CITY_DAY_PATH, index=False, date_format="%Y-%m-%d")
    return CLEANED_CITY_DAY_PATH
