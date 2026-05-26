# AirLens — Climate-Tech Research & Outreach Intelligence Platform

AirLens is a full-stack climate-tech research workspace that converts real Indian air quality datasets into AQI dashboards, research briefs, public communication drafts, stakeholder outreach records, research notes, biofiltration observations, and exportable reports.

The project was built around a real-world research and outreach workflow for air pollution and climate-tech teams. Instead of being only a dashboard, AirLens connects data analysis, documentation, reporting, content drafting, and stakeholder coordination in one workspace.

---

## Project Purpose

Air pollution research often involves multiple disconnected tasks:

- collecting and cleaning air quality datasets
- analyzing pollutant trends
- preparing research notes and reports
- creating public communication material
- maintaining stakeholder outreach records
- documenting intervention observations
- exporting findings for presentations or reports

AirLens brings these workflows into a single platform designed for climate-tech research, documentation, and outreach use cases.

---

## Key Features

### Dataset Upload and Cleaning

- Upload real `city_day.csv` air quality data
- Validate required columns such as City, Date/Datetime, and AQI
- Detect supported pollutant columns
- Remove duplicate records
- Convert dates and numeric pollutant fields
- Fill missing pollutant values using city-wise median and overall median
- Generate a data quality summary
- Store cleaned dataset for downstream analysis

### AQI and Pollutant Dashboard

- City-wise AQI summary
- AQI trend visualization
- PM2.5 and PM10 comparison
- Pollutant-wise average comparison
- AQI bucket distribution
- Worst pollution days
- Simple anomaly detection using AQI thresholding

### Research Brief Generator

- Generates structured research briefs from computed AQI metrics
- Includes objective, methodology, key findings, pollutant interpretation, limitations, and conclusion
- Supports technical, public, and stakeholder-oriented summaries
- Uses computed dataset metrics instead of dummy or hardcoded numbers

### Content Studio

- Generates communication drafts from real pollution analysis
- Supports blog drafts, awareness points, LinkedIn-style posts, and stakeholder notes
- Helps convert research findings into public-facing communication material

### Outreach CRM

- Add and manage stakeholder contacts
- Track NGOs, colleges, researchers, government bodies, and climate groups
- Maintain outreach status, notes, contact details, and follow-up dates
- Generate outreach email drafts using city-level air quality insights

### Research Log

- Maintain research activity records
- Store source names, URLs, summaries, tags, and status
- Track research notes, article references, dataset observations, and draft ideas

### Biofiltration / Intervention Comparison

- Document before-and-after pollutant observations
- Calculate reduction percentage
- Generate observation notes
- Designed as a software documentation module, not a physical hardware implementation

### Report Export

- Generate Markdown research reports
- Generate LaTeX report source
- Useful for technical documentation and research-style reporting

---

## Tech Stack

### Frontend

- Next.js
- TypeScript
- Tailwind CSS
- Recharts
- Lucide React

### Backend

- FastAPI
- Python
- Pandas
- NumPy
- SQLAlchemy
- SQLite

### Tools

- Git
- GitHub
- VS Code
- Render
- Vercel

---

## Dataset

AirLens is designed for the **Air Quality in India 2015–2024** dataset.

Primary file used:

```text
city_day.csv
