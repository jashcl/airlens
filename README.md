# AirLens — Climate-Tech Research & Outreach Intelligence Platform

AirLens is a full-stack climate-tech workspace that converts real Indian air quality data into dashboards, research briefs, content drafts, stakeholder outreach records, research notes, biofiltration comparison observations, and Markdown/LaTeX reports.

## Live Demo
- Frontend: add Vercel URL here
- Backend API: add Render URL here

## Problem Statement
Air pollution research often requires cleaning spreadsheets, analyzing pollutant trends, writing reports, preparing public communication, and managing outreach records separately. AirLens combines these workflows into one research-to-communication platform.

## Dataset
Primary dataset: Air Quality in India 2015–2024. Main file used: `city_day.csv`.

Expected columns include City, Date/Datetime, AQI, PM2.5, PM10, NO, NO2, NOx, NH3, CO, SO2, O3, and AQI_Bucket.

## Features
- Real CSV upload and validation
- Data cleaning summary with missing values before/after
- AQI trend dashboard and pollutant charts
- Worst pollution days and anomaly detection
- Research brief generation from computed metrics
- Blog, LinkedIn, awareness, and stakeholder draft generation
- Outreach CRM for stakeholder records and email drafts
- Research log for sources and activity notes
- Biofiltration/intervention before-after comparison
- Markdown and LaTeX export

## Tech Stack
Frontend: Next.js, TypeScript, Tailwind CSS, Recharts  
Backend: FastAPI, Python, Pandas, SQLAlchemy, SQLite  
Deployment: Vercel frontend, Render backend

## Local Setup

Backend:
```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Frontend:
```bash
cd frontend
npm install
npm run dev
```

Open frontend at `http://localhost:3000` and backend docs at `http://127.0.0.1:8000/docs`.

## Deployment
Backend on Render:
- Root directory: `backend`
- Build command: `pip install -r requirements.txt`
- Start command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
- Env var: `FRONTEND_URL=https://your-vercel-url.vercel.app`

Frontend on Vercel:
- Root directory: `frontend`
- Env var: `NEXT_PUBLIC_API_BASE_URL=https://your-render-backend.onrender.com`

## Limitations
For demo deployment, uploaded CSV files are stored locally on the backend service. Free Render instances may reset local files, so users may need to upload the dataset again after service restart. In production, use PostgreSQL and object storage such as S3.

## Future Scope
- OpenAQ API integration
- Hourly analysis using `city_hour.csv`
- Station-level analysis
- PDF report generation
- Authentication and persistent multi-user workspaces
