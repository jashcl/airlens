"""CSV loading and source-column validation services."""

from io import BytesIO

import pandas as pd


REQUIRED_COLUMNS = ("City", "Date", "AQI")
DATE_COLUMN_ALIASES = ("Datetime",)
POLLUTANT_COLUMNS = ("PM2.5", "PM10", "NO", "NO2", "NOx", "NH3", "CO", "SO2", "O3")


def load_city_day_csv(content: bytes) -> pd.DataFrame:
    """Load and validate an uploaded city-day CSV file."""
    try:
        dataframe = pd.read_csv(BytesIO(content), encoding="utf-8-sig")
    except pd.errors.EmptyDataError as exc:
        raise ValueError("The uploaded CSV file is empty.") from exc
    except (UnicodeDecodeError, pd.errors.ParserError) as exc:
        raise ValueError("The uploaded file could not be read as a valid CSV.") from exc

    if dataframe.empty:
        raise ValueError("The uploaded CSV file contains no data rows.")

    dataframe = _normalise_date_column(dataframe)
    _validate_required_columns(dataframe)
    return dataframe


def detected_pollutant_columns(dataframe: pd.DataFrame) -> list[str]:
    """Return supported pollutant fields that are present in the source."""
    return [column for column in POLLUTANT_COLUMNS if column in dataframe.columns]


def _normalise_date_column(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Map a known source date alias into the application's Date field."""
    if "Date" in dataframe.columns:
        return dataframe

    for alias in DATE_COLUMN_ALIASES:
        if alias in dataframe.columns:
            return dataframe.rename(columns={alias: "Date"})

    return dataframe


def _validate_required_columns(dataframe: pd.DataFrame) -> None:
    missing_columns = [
        column for column in REQUIRED_COLUMNS if column not in dataframe.columns
    ]
    if missing_columns:
        required = ", ".join(REQUIRED_COLUMNS)
        missing = ", ".join(missing_columns)
        raise ValueError(
            f"Missing required column(s): {missing}. Required columns are: {required}."
        )
