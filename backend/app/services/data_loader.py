from pathlib import Path
import pandas as pd
from fastapi import HTTPException, UploadFile
from .data_cleaning import clean_air_quality_dataframe, dataframe_response, normalize_columns, validate_dataframe
from ..utils.file_storage import save_upload, latest_cleaned_path

async def process_upload(file: UploadFile) -> dict:
    if not file.filename or not file.filename.lower().endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only .csv files are supported.")
    # Validate before saving as latest source.
    raw_content = await file.read()
    if not raw_content:
        raise HTTPException(status_code=400, detail="Uploaded file is empty.")
    tmp = Path("_tmp_airlens_upload.csv")
    tmp.write_bytes(raw_content)
    try:
        raw_df = pd.read_csv(tmp)
        raw_df = normalize_columns(raw_df)
        validate_dataframe(raw_df)
        cleaned_df, summary = clean_air_quality_dataframe(raw_df)
    except pd.errors.EmptyDataError:
        raise HTTPException(status_code=400, detail="Uploaded CSV is empty or unreadable.")
    finally:
        tmp.unlink(missing_ok=True)
    # Persist after validation succeeds.
    upload_path = Path(__file__).resolve().parent.parent.parent / "data" / "uploads" / Path(file.filename).name
    upload_path.write_bytes(raw_content)
    cleaned_df.to_csv(latest_cleaned_path(), index=False)
    return dataframe_response(cleaned_df, summary, Path(file.filename).name)

def load_latest_cleaned() -> pd.DataFrame:
    path = latest_cleaned_path()
    if not path.exists():
        raise HTTPException(status_code=404, detail="No cleaned dataset found. Upload city_day.csv first from the Datasets page.")
    df = pd.read_csv(path)
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    return df
