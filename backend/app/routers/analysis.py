from fastapi import APIRouter
from pydantic import BaseModel
from ..services import eda_service as eda

router = APIRouter(prefix="/analysis", tags=["analysis"])

class CompareRequest(BaseModel):
    cities: list[str]
    pollutant: str

@router.get("/cities")
def cities(): return {"cities": eda.get_available_cities()}
@router.get("/summary/{city}")
def summary(city: str): return eda.get_city_summary(city)
@router.get("/aqi-trend/{city}")
def aqi_trend(city: str): return eda.get_aqi_trend(city)
@router.get("/pollutant-trend/{city}/{pollutant}")
def pollutant_trend(city: str, pollutant: str): return eda.get_pollutant_trend(city, pollutant)
@router.get("/pm25-pm10/{city}")
def pm25_pm10(city: str): return eda.get_pm25_pm10(city)
@router.get("/pollutant-comparison/{city}")
def pollutant_comparison(city: str): return eda.get_pollutant_comparison(city)
@router.get("/aqi-buckets/{city}")
def buckets(city: str): return eda.get_aqi_buckets(city)
@router.get("/worst-days/{city}")
def worst_days(city: str, limit: int = 10): return eda.get_worst_days(city, limit)
@router.get("/anomalies/{city}")
def anomalies(city: str): return eda.get_anomalies(city)
@router.post("/compare-cities")
def compare(req: CompareRequest): return eda.compare_cities(req.cities, req.pollutant)
