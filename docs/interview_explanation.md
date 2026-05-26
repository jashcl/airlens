# AirLens Interview Explanation

## 2-minute version
I built AirLens because the internship requires research, documentation, data analysis, visualization, and outreach. Instead of making only an AQI dashboard, I designed it as a complete research-to-communication workflow for a climate-tech team. The app uploads a real Indian air quality dataset, cleans it using Python/Pandas, visualizes AQI and pollutant trends, generates research briefs, creates outreach/content drafts, and tracks stakeholder and research records.

## Technical choices
FastAPI was used because the backend needed Python-based data handling. Pandas handles cleaning and EDA. Next.js and Tailwind make the frontend look like a real internal SaaS tool. SQLite keeps the MVP simple and defendable.

## Data cleaning
The app validates City, Date/Datetime, and AQI. It parses dates, removes duplicates, converts pollutants to numeric, and fills pollutant gaps using city-wise median with overall median fallback.

## Limitations
It documents observations and does not claim hardware implementation. Uploaded file storage is local in the demo and should be replaced with object storage in production.
