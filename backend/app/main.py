"""FastAPI application entrypoint for AirLens."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import (
    analysis,
    biofiltration,
    content,
    datasets,
    outreach,
    reports,
    research_log,
)
from app.schemas import HealthResponse


app = FastAPI(
    title="AirLens API",
    description="Backend API for climate-tech research and outreach intelligence.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health", response_model=HealthResponse, tags=["Health"])
def health_check() -> HealthResponse:
    """Return the API availability status."""
    return HealthResponse(status="ok")


app.include_router(datasets.router)
app.include_router(analysis.router)
app.include_router(reports.router)
app.include_router(content.router)
app.include_router(outreach.router)
app.include_router(research_log.router)
app.include_router(biofiltration.router)
