import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine
from .routers import datasets, analysis, reports, content, outreach, research_log, biofiltration

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AirLens API", version="1.0.0")
origins = ["http://localhost:3000", "http://127.0.0.1:3000"]
if os.getenv("FRONTEND_URL"):
    origins.append(os.getenv("FRONTEND_URL"))
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.get("/")
def root(): return {"app": "AirLens API", "status": "running", "docs": "/docs", "health": "/health"}
@app.get("/health")
def health(): return {"status": "ok"}

app.include_router(datasets.router)
app.include_router(analysis.router)
app.include_router(reports.router)
app.include_router(content.router)
app.include_router(outreach.router)
app.include_router(research_log.router)
app.include_router(biofiltration.router)
