# AirLens — Climate-Tech Research Platform

AirLens is a full-stack research platform that turns real Indian air quality data into dashboards, research briefs, content drafts, outreach records, research notes, biofiltration observations, and exportable reports.

## Problem Statement

Air pollution research usually does not stop at analysis. The same data often needs to be cleaned, visualized, documented, summarized for non-technical audiences, shared with stakeholders, and converted into reports.

Most projects solve only one part of this workflow. AirLens connects the complete flow from raw dataset to research output and outreach material.

## What the Project Does

AirLens allows a user to upload `city_day.csv`, clean the dataset, analyze AQI and pollutant trends, generate research briefs, create public communication drafts, maintain outreach records, store research notes, compare before/after pollutant observations, and export reports in Markdown and LaTeX.

## Key Features

### Dataset Upload and Cleaning

- Uploads real `city_day.csv` air quality data
- Validates required columns such as City, Date/Datetime, and AQI
- Detects supported pollutant columns
- Removes duplicate records
- Converts dates and numeric pollutant fields
- Fills missing pollutant values using city-wise median and overall median
- Generates a data quality summary
- Stores cleaned data for analysis

### AQI and Pollutant Dashboard

- Shows city-wise AQI summaries
- Visualizes AQI trends
- Compares PM2.5 and PM10
- Shows pollutant-wise average values
- Displays AQI bucket distribution
- Lists worst pollution days
- Detects simple AQI anomalies

### Research Brief Generator

- Generates structured research briefs from computed AQI metrics
- Includes objective, methodology, key findings, pollutant interpretation, limitations, and conclusion
- Supports technical, public, and stakeholder-oriented summaries
- Uses actual dataset metrics instead of dummy values

### Content Studio

- Creates blog drafts, awareness points, LinkedIn-style posts, and stakeholder notes
- Uses computed pollution insights as input
- Helps convert analysis into public-facing communication material

### Outreach CRM

- Stores stakeholder contacts
- Tracks NGOs, colleges, researchers, government bodies, and climate groups
- Maintains outreach status, notes, contact details, and follow-up dates
- Generates outreach email drafts using city-level air quality insights

### Research Log

- Stores research notes, source names, source URLs, summaries, tags, and status
- Helps maintain a record of research activities and content drafts

### Biofiltration / Intervention Comparison

- Documents before-and-after pollutant observations
- Calculates reduction percentage
- Generates observation notes
- Works as a software documentation module, not a hardware control system

### Report Export

- Generates Markdown research reports
- Generates LaTeX report source
- Supports technical documentation and research-style reporting

## Tech Stack

**Frontend:** Next.js, TypeScript, Tailwind CSS, Recharts, Lucide React  
**Backend:** FastAPI, Python, Pandas, NumPy, SQLAlchemy, SQLite  
**Tools:** Git, GitHub, VS Code, Render, Vercel

## Dataset / Input Requirements

AirLens is designed for the **Air Quality in India 2015–2024** dataset.

Use this file:

```text
city_day.csv
```

Expected columns:

```text
City
Date or Datetime
PM2.5
PM10
NO
NO2
NOx
NH3
CO
SO2
O3
AQI
AQI_Bucket
```

The app accepts `Datetime` as an alias and normalizes it to `Date` during processing.

The full dataset is not included in this repository because it is large. Download the dataset separately and upload `city_day.csv` through the app’s **Datasets** page.

## Project Architecture

```text
airlens/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── routers/
│   │   │   ├── datasets.py
│   │   │   ├── analysis.py
│   │   │   ├── reports.py
│   │   │   ├── content.py
│   │   │   ├── outreach.py
│   │   │   ├── research_log.py
│   │   │   └── biofiltration.py
│   │   ├── services/
│   │   └── utils/
│   │
│   ├── data/
│   │   ├── uploads/
│   │   └── processed/
│   │
│   └── requirements.txt
│
├── frontend/
│   ├── app/
│   ├── components/
│   ├── lib/
│   └── package.json
│
├── docs/
├── sample_data/
├── README.md
└── .gitignore
```

## How to Run Locally

Run the backend and frontend in two separate terminals.

### Prerequisites

Install:

```text
Python 3.10+
Node.js 20+
Git
```

Check versions:

```bash
python --version
node -v
npm -v
git --version
```

### 1. Clone the Repository

```bash
git clone https://github.com/jashcl/airlens.git
cd airlens
```

### 2. Start the Backend

Open the first terminal:

```bash
cd backend
python -m venv .venv
```

Activate the virtual environment.

For Windows:

```bash
.venv\Scripts\activate
```

For macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the backend:

```bash
uvicorn app.main:app --reload
```

Backend runs at:

```text
http://127.0.0.1:8000
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

Keep this terminal running.

### 3. Start the Frontend

Open a second terminal from the project root:

```bash
cd frontend
npm install
```

Create a `.env.local` file inside the `frontend` folder:

```env
NEXT_PUBLIC_API_BASE_URL=http://127.0.0.1:8000
```

Run the frontend:

```bash
npm run dev
```

Frontend runs at:

```text
http://localhost:3000
```

## How to Use the App

Open:

```text
http://localhost:3000
```

Recommended flow:

```text
Datasets → Dashboard → Research Brief → Content Studio → Outreach CRM → Research Log → Biofiltration → Reports
```

Start with the **Datasets** page. Upload `city_day.csv`, review the cleaning summary, then move to the dashboard and other modules.

## API Routes / Backend Overview

```text
GET  /
POST /datasets/upload

GET  /analysis/cities
GET  /analysis/summary/{city}
GET  /analysis/aqi-trend/{city}
GET  /analysis/pm25-pm10/{city}
GET  /analysis/pollutant-comparison/{city}
GET  /analysis/aqi-buckets/{city}
GET  /analysis/worst-days/{city}
GET  /analysis/anomalies/{city}

POST /reports/research-brief
GET  /reports/{city}/markdown
GET  /reports/{city}/latex

POST /content/blog-draft
POST /content/linkedin-post
POST /content/awareness-points
POST /content/stakeholder-note

POST /outreach/stakeholders
GET  /outreach/stakeholders
POST /outreach/stakeholders/{id}/generate-email

POST /research-log
GET  /research-log

POST /biofiltration/compare
GET  /biofiltration/records
```

## Data Cleaning Methodology

AirLens applies a simple and explainable cleaning workflow:

1. Validates CSV file type
2. Checks required columns
3. Accepts `Date` or `Datetime`
4. Converts date values to datetime format
5. Converts AQI and pollutant fields to numeric values
6. Removes duplicate rows
7. Fills missing pollutant values using city-wise median
8. Falls back to overall median where city-wise median is unavailable
9. Sorts records by city and date
10. Stores a cleaned dataset for analysis

This approach is transparent and easy to explain.

## Analysis Methodology

AirLens computes:

- city-level AQI summaries
- average, minimum, and maximum AQI
- pollutant averages
- PM2.5 and PM10 trends
- AQI bucket distributions
- worst pollution days
- simple AQI anomaly flags

Anomalies are detected using:

```text
AQI > mean AQI + 2 * standard deviation
```

This rule is simple and suitable for an MVP analysis workflow.

## Design Decisions

- FastAPI was used because the backend depends on Python-based data cleaning and analysis.
- Pandas was used for CSV validation, missing-value handling, and city-wise analysis.
- Next.js was used to build a clean dashboard-style interface.
- SQLite was used for MVP simplicity.
- Content generation is template-based so the output stays explainable and does not invent analysis numbers.
- Biofiltration is handled as an observation and documentation module, not a hardware implementation.

## Limitations

- The full dataset must be downloaded separately.
- SQLite is used for MVP simplicity.
- Uploaded files are stored locally during development.
- The content generation system is template-based and does not use external AI APIs.
- Biofiltration comparison is a documentation module, not a hardware control system.
- Maps and real-time AQI APIs are not included in the MVP.

## Future Scope

- Add OpenAQ or CPCB API integration
- Add persistent cloud storage for uploaded datasets
- Replace SQLite with PostgreSQL
- Add map-based AQI visualization
- Add PDF report export
- Add email reminder workflows for outreach follow-ups
- Add user authentication
- Add station-level pollution analysis
- Add hourly pollution pattern analysis using `city_hour.csv`

## Project Status

MVP completed.

Current version supports dataset upload, data cleaning, AQI dashboarding, research brief generation, content drafting, stakeholder outreach tracking, research logs, biofiltration comparison, and Markdown/LaTeX report generation.

## Author

**Jash Shah**  
B.Tech Information Technology  
Dwarkadas J. Sanghvi College of Engineering, Mumbai

GitHub: [jashcl](https://github.com/jashcl)
