from __future__ import annotations
import pandas as pd
from fastapi import HTTPException

REQUIRED_COLUMNS = {"City", "Date", "AQI"}
DATE_ALIASES = {"Datetime": "Date", "date": "Date", "datetime": "Date"}
POLLUTANTS = ["PM2.5", "PM10", "NO", "NO2", "NOx", "NH3", "CO", "SO2", "O3"]

def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    rename = {}
    for col in df.columns:
        if col in DATE_ALIASES:
            rename[col] = DATE_ALIASES[col]
        elif col.strip() != col:
            rename[col] = col.strip()
    return df.rename(columns=rename)

def validate_dataframe(df: pd.DataFrame) -> None:
    if df.empty:
        raise HTTPException(status_code=400, detail="Uploaded CSV is empty.")
    missing = sorted(REQUIRED_COLUMNS - set(df.columns))
    if missing:
        raise HTTPException(status_code=400, detail=f"Missing required columns: {', '.join(missing)}")

def clean_air_quality_dataframe(df: pd.DataFrame):
    original_rows = len(df)
    df = normalize_columns(df)
    validate_dataframe(df)
    missing_before = df.isna().sum().astype(int).to_dict()
    before_dedup = len(df)
    df = df.drop_duplicates().copy()
    duplicate_rows_removed = before_dedup - len(df)
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    if df["Date"].isna().all():
        raise HTTPException(status_code=400, detail="Date column could not be parsed.")
    df = df.dropna(subset=["City", "Date"])
    numeric_cols = [c for c in ["AQI"] + POLLUTANTS if c in df.columns]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    for col in [c for c in POLLUTANTS if c in df.columns]:
        df[col] = df.groupby("City")[col].transform(lambda s: s.fillna(s.median()))
        overall = df[col].median()
        if pd.notna(overall):
            df[col] = df[col].fillna(overall)
    # AQI remains factual; do not fabricate if missing, but drop rows with no AQI for analysis.
    df = df.dropna(subset=["AQI"])
    df = df.sort_values(["City", "Date"]).reset_index(drop=True)
    missing_after = df.isna().sum().astype(int).to_dict()
    summary = {
        "original_rows": int(original_rows),
        "cleaned_rows": int(len(df)),
        "duplicate_rows_removed": int(duplicate_rows_removed),
        "missing_values_before": missing_before,
        "missing_values_after": missing_after,
    }
    return df, summary

def dataframe_response(df: pd.DataFrame, summary: dict, filename: str) -> dict:
    pollutants = [c for c in POLLUTANTS if c in df.columns]
    preview = df.head(10).copy()
    preview["Date"] = preview["Date"].dt.strftime("%Y-%m-%d")
    return {
        "filename": filename,
        **summary,
        "columns": list(df.columns),
        "detected_cities": sorted(df["City"].dropna().astype(str).unique().tolist()),
        "detected_pollutants": pollutants,
        "min_date": df["Date"].min().strftime("%Y-%m-%d"),
        "max_date": df["Date"].max().strftime("%Y-%m-%d"),
        "preview_rows": preview.where(pd.notnull(preview), None).to_dict(orient="records"),
    }
