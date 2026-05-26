"""Deterministic cleaning and data-quality summarisation for city-day data."""

import json
from dataclasses import dataclass

import pandas as pd

from app.services.data_loader import detected_pollutant_columns


@dataclass
class CleaningResult:
    """Cleaned dataset plus values required by the API summary."""

    dataframe: pd.DataFrame
    original_rows: int
    duplicate_rows_removed: int
    missing_values_before: dict[str, int]
    missing_values_after: dict[str, int]
    detected_cities: list[str]
    detected_pollutants: list[str]
    min_date: str
    max_date: str
    preview_rows: list[dict[str, object]]

    @property
    def cleaned_rows(self) -> int:
        return len(self.dataframe)


def clean_city_day_data(dataframe: pd.DataFrame) -> CleaningResult:
    """Apply the agreed cleaning rules and prepare a quality summary."""
    original_rows = len(dataframe)
    missing_values_before = _missing_value_counts(dataframe)
    detected_pollutants = detected_pollutant_columns(dataframe)

    cleaned = dataframe.drop_duplicates().copy()
    duplicate_rows_removed = original_rows - len(cleaned)

    cleaned["Date"] = _parse_date_column(cleaned["Date"])

    numeric_columns = ["AQI", *detected_pollutants]
    for column in numeric_columns:
        cleaned[column] = pd.to_numeric(cleaned[column], errors="coerce")

    for pollutant in detected_pollutants:
        city_median = cleaned.groupby("City")[pollutant].transform("median")
        overall_median = cleaned[pollutant].median()
        cleaned[pollutant] = cleaned[pollutant].fillna(city_median)
        cleaned[pollutant] = cleaned[pollutant].fillna(overall_median)

    cleaned = cleaned.sort_values(["City", "Date"], na_position="last").reset_index(
        drop=True
    )

    return CleaningResult(
        dataframe=cleaned,
        original_rows=original_rows,
        duplicate_rows_removed=duplicate_rows_removed,
        missing_values_before=missing_values_before,
        missing_values_after=_missing_value_counts(cleaned),
        detected_cities=_detected_cities(cleaned),
        detected_pollutants=detected_pollutants,
        min_date=cleaned["Date"].min().strftime("%Y-%m-%d"),
        max_date=cleaned["Date"].max().strftime("%Y-%m-%d"),
        preview_rows=_preview_rows(cleaned),
    )


def _parse_date_column(date_column: pd.Series) -> pd.Series:
    parsed_dates = pd.to_datetime(date_column, errors="coerce")
    invalid_dates = int(parsed_dates.isna().sum())
    if invalid_dates:
        raise ValueError(
            "Date column contains "
            f"{invalid_dates} missing or invalid value(s). Every Date must be parseable."
        )
    return parsed_dates


def _missing_value_counts(dataframe: pd.DataFrame) -> dict[str, int]:
    return {
        column: int(count)
        for column, count in dataframe.isna().sum().to_dict().items()
    }


def _detected_cities(dataframe: pd.DataFrame) -> list[str]:
    cities = dataframe["City"].dropna().astype(str).unique().tolist()
    return sorted(cities)


def _preview_rows(dataframe: pd.DataFrame) -> list[dict[str, object]]:
    preview = dataframe.head(10).copy()
    preview["Date"] = preview["Date"].dt.strftime("%Y-%m-%d")
    return json.loads(preview.to_json(orient="records"))
