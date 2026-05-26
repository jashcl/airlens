# AirLens Codex Instructions

We are building AirLens, a full-stack climate-tech research and outreach intelligence platform.

The project is designed for a Research and Outreach Internship at an air pollution / climate-tech company.

The app should convert real Indian air quality data into:
- data quality summaries
- AQI and pollutant dashboards
- research briefs
- blog/article drafts
- public awareness content
- stakeholder outreach drafts
- research activity records
- biofiltration/intervention comparison notes
- Markdown and LaTeX reports

Main dataset:
- Air Quality in India 2015-2024
- Primary file: city_day.csv

Expected city_day.csv columns:
- City
- Date
- PM2.5
- PM10
- NO
- NO2
- NOx
- NH3
- CO
- SO2
- O3
- AQI
- AQI_Bucket

Tech stack:
- Frontend: Next.js, TypeScript, Tailwind CSS, Recharts, lucide-react
- Backend: FastAPI, Python, Pandas, NumPy, SQLAlchemy, SQLite
- Reports: Markdown first, LaTeX second, PDF later
- Deployment: Frontend on Vercel, backend on Render

Main pages:
1. Overview
2. Datasets
3. Dashboard
4. Research Brief
5. Content Studio
6. Outreach CRM
7. Research Log
8. Biofiltration
9. Reports
10. Settings

Development principles:
- Keep code clean, modular, and easy to explain in interviews.
- Do not over-engineer.
- Do not add authentication in MVP.
- Do not add payment or user accounts.
- Do not use external AI APIs in MVP.
- Use deterministic template-based content generation from real computed metrics.
- Never invent analysis numbers.
- All generated reports/content should be based on actual dataset metrics.
- Use clear loading, error, and empty states.
- Make UI look like a polished climate-tech SaaS/internal research tool.
- For biofiltration, frame it as a software module for documenting before/after observations, not physical hardware.

Data cleaning rules:
- Validate required columns: City, Date, AQI.
- Parse Date as datetime.
- Convert AQI and pollutant columns to numeric.
- Remove duplicate rows.
- Fill missing numeric pollutant values using city-wise median.
- If city-wise median is unavailable, use overall median.
- Do not blindly fill City or Date.
- Return missing values before and after cleaning.

Analysis rules:
- Use latest cleaned CSV from backend/data/processed.
- Compute city summary.
- Compute AQI trend.
- Compute pollutant comparison.
- Compute AQI bucket distribution.
- Compute worst pollution days.
- Detect AQI anomalies using AQI > mean + 2 * standard deviation.
- Keep logic simple and defendable.

UI style:
- Modern SaaS dashboard.
- Dark sidebar.
- Clean light main area.
- Green/teal accent.
- Rounded cards.
- Professional charts.
- Strong empty states.
- Great screenshots for resume/GitHub.

Always inspect current project files before editing.
After every feature, run relevant checks and fix errors.
Update docs/TODO.md after each milestone.