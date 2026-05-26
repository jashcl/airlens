from __future__ import annotations
import pandas as pd
from fastapi import HTTPException
from .data_loader import load_latest_cleaned
from .aqi_rules import classify_aqi

POLLUTANTS = ["PM2.5", "PM10", "NO", "NO2", "NOx", "NH3", "CO", "SO2", "O3"]

def _df(): return load_latest_cleaned()

def _city_df(city: str) -> pd.DataFrame:
    df = _df()
    cdf = df[df["City"].astype(str).str.lower() == city.lower()].copy()
    if cdf.empty:
        raise HTTPException(status_code=404, detail=f"City '{city}' not found in dataset.")
    return cdf

def _json_records(df: pd.DataFrame):
    out = df.copy()
    for col in out.columns:
        if pd.api.types.is_datetime64_any_dtype(out[col]):
            out[col] = out[col].dt.strftime("%Y-%m-%d")
    return out.where(pd.notnull(out), None).to_dict(orient="records")

def get_available_cities():
    df = _df()
    return sorted(df["City"].dropna().astype(str).unique().tolist())

def get_city_summary(city: str):
    cdf = _city_df(city)
    worst = cdf.loc[cdf["AQI"].idxmax()]
    best = cdf.loc[cdf["AQI"].idxmin()]
    available_pollutants = [p for p in POLLUTANTS if p in cdf.columns]
    bucket = cdf["AQI_Bucket"].mode().iloc[0] if "AQI_Bucket" in cdf and not cdf["AQI_Bucket"].dropna().empty else classify_aqi(float(cdf["AQI"].mean()))
    return {
        "city": city,
        "total_records": int(len(cdf)),
        "min_date": cdf["Date"].min().strftime("%Y-%m-%d"),
        "max_date": cdf["Date"].max().strftime("%Y-%m-%d"),
        "average_aqi": round(float(cdf["AQI"].mean()), 2),
        "max_aqi": round(float(cdf["AQI"].max()), 2),
        "min_aqi": round(float(cdf["AQI"].min()), 2),
        "dominant_aqi_bucket": str(bucket),
        "average_pm25": round(float(cdf["PM2.5"].mean()), 2) if "PM2.5" in cdf else None,
        "average_pm10": round(float(cdf["PM10"].mean()), 2) if "PM10" in cdf else None,
        "worst_day": {"date": worst["Date"].strftime("%Y-%m-%d"), "aqi": round(float(worst["AQI"]), 2)},
        "best_day": {"date": best["Date"].strftime("%Y-%m-%d"), "aqi": round(float(best["AQI"]), 2)},
        "available_pollutants": available_pollutants,
    }

def get_aqi_trend(city: str):
    cdf = _city_df(city)[["Date", "AQI"]].copy()
    cdf["AQI"] = cdf["AQI"].round(2)
    return _json_records(cdf)

def get_pollutant_trend(city: str, pollutant: str):
    cdf = _city_df(city)
    if pollutant not in cdf.columns:
        raise HTTPException(status_code=400, detail=f"Pollutant not available. Available: {', '.join([p for p in POLLUTANTS if p in cdf.columns])}")
    out = cdf[["Date", pollutant]].copy()
    out[pollutant] = out[pollutant].round(2)
    return _json_records(out)

def get_pm25_pm10(city: str):
    cdf = _city_df(city)
    cols = ["Date"] + [c for c in ["PM2.5", "PM10"] if c in cdf.columns]
    out = cdf[cols].copy()
    for c in cols[1:]: out[c] = out[c].round(2)
    return _json_records(out)

def get_pollutant_comparison(city: str):
    cdf = _city_df(city)
    rows=[]
    for p in POLLUTANTS:
        if p in cdf.columns:
            rows.append({"pollutant": p, "average_value": round(float(cdf[p].mean()), 2)})
    return rows

def get_aqi_buckets(city: str):
    cdf = _city_df(city).copy()
    if "AQI_Bucket" not in cdf.columns:
        cdf["AQI_Bucket"] = cdf["AQI"].apply(classify_aqi)
    counts = cdf["AQI_Bucket"].fillna("Unknown").value_counts().reset_index()
    counts.columns = ["bucket", "count"]
    return counts.to_dict(orient="records")

def get_worst_days(city: str, limit: int = 10):
    cdf = _city_df(city)
    cols = [c for c in ["Date", "AQI", "AQI_Bucket", "PM2.5", "PM10"] if c in cdf.columns]
    out = cdf.sort_values("AQI", ascending=False).head(limit)[cols].copy()
    return _json_records(out)

def get_anomalies(city: str):
    cdf = _city_df(city)
    threshold = cdf["AQI"].mean() + 2 * cdf["AQI"].std()
    out = cdf[cdf["AQI"] > threshold][[c for c in ["Date", "AQI", "AQI_Bucket", "PM2.5", "PM10"] if c in cdf.columns]].copy()
    out = out.sort_values("AQI", ascending=False).head(25)
    return {"threshold": round(float(threshold), 2), "count": int(len(out)), "records": _json_records(out)}

def compare_cities(cities: list[str], pollutant: str):
    df = _df()
    if pollutant not in df.columns:
        raise HTTPException(status_code=400, detail="Pollutant not available in dataset.")
    rows=[]
    for city in cities:
        cdf=df[df["City"].astype(str).str.lower()==city.lower()]
        if not cdf.empty:
            rows.append({"city": city, "average_value": round(float(cdf[pollutant].mean()), 2)})
    return rows
