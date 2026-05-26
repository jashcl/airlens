"""Dataset management routes."""

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.schemas import DatasetUploadSummary
from app.services.data_cleaning import clean_city_day_data
from app.services.data_loader import load_city_day_csv
from app.utils.file_storage import (
    save_cleaned_dataset,
    save_uploaded_file,
    validate_csv_filename,
    validate_upload_content,
)


router = APIRouter(prefix="/datasets", tags=["Datasets"])


@router.post("/upload", response_model=DatasetUploadSummary)
async def upload_dataset(file: UploadFile = File(...)) -> DatasetUploadSummary:
    """Store, validate, and clean an uploaded city-level daily CSV dataset."""
    try:
        filename = validate_csv_filename(file.filename)
        content = await file.read()
        validate_upload_content(content)
        source_data = load_city_day_csv(content)
        result = clean_city_day_data(source_data)
        uploaded_file_path = save_uploaded_file(filename, content)
        save_cleaned_dataset(result.dataframe)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    return DatasetUploadSummary(
        filename=uploaded_file_path.name,
        original_rows=result.original_rows,
        cleaned_rows=result.cleaned_rows,
        duplicate_rows_removed=result.duplicate_rows_removed,
        columns=result.dataframe.columns.tolist(),
        missing_values_before=result.missing_values_before,
        missing_values_after=result.missing_values_after,
        detected_cities=result.detected_cities,
        detected_pollutants=result.detected_pollutants,
        min_date=result.min_date,
        max_date=result.max_date,
        preview_rows=result.preview_rows,
    )
