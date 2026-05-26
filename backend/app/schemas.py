"""Pydantic request and response schemas."""

from typing import Any

from pydantic import BaseModel


class HealthResponse(BaseModel):
    """Response returned by the health endpoint."""

    status: str


class DatasetUploadSummary(BaseModel):
    """Cleaning and data-quality summary for an uploaded city-day dataset."""

    filename: str
    original_rows: int
    cleaned_rows: int
    duplicate_rows_removed: int
    columns: list[str]
    missing_values_before: dict[str, int]
    missing_values_after: dict[str, int]
    detected_cities: list[str]
    detected_pollutants: list[str]
    min_date: str
    max_date: str
    preview_rows: list[dict[str, Any]]
