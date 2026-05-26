from .eda_service import get_city_summary, get_pollutant_comparison, get_worst_days, get_anomalies

def _find_metric(rows, pollutant):
    for r in rows:
        if r["pollutant"] == pollutant: return r["average_value"]
    return None

def build_research_brief(city: str, audience: str = "technical"):
    s = get_city_summary(city)
    comps = get_pollutant_comparison(city)
    worst = get_worst_days(city, 3)
    anomalies = get_anomalies(city)
    pm25 = _find_metric(comps, "PM2.5")
    pm10 = _find_metric(comps, "PM10")
    title = f"Air Quality Research Brief — {city}"
    key_findings = [
        f"Average AQI for {city} is {s['average_aqi']} across {s['total_records']} daily records.",
        f"The highest recorded AQI is {s['max_aqi']} on {s['worst_day']['date']}.",
        f"Dominant AQI bucket in the selected dataset is {s['dominant_aqi_bucket']}.",
        f"Detected {anomalies['count']} unusually high AQI days using a mean + 2σ rule.",
    ]
    if pm25 is not None: key_findings.append(f"Average PM2.5 concentration is {pm25} in the cleaned dataset.")
    if pm10 is not None: key_findings.append(f"Average PM10 concentration is {pm10} in the cleaned dataset.")
    executive = f"This brief summarizes city-level air quality trends for {city} using cleaned daily records from {s['min_date']} to {s['max_date']}. The analysis focuses on AQI, pollutant averages, worst pollution days, and simple anomaly flags to support research documentation and outreach planning."
    pollution_lines = "\n".join([f"- {r['pollutant']}: average {r['average_value']}" for r in comps])
    findings_lines = "\n".join([f"- {k}" for k in key_findings])
    worst_lines = "\n".join([f"- {r.get('Date')}: AQI {r.get('AQI')}" for r in worst])
    markdown = f"""# {title}

## Objective
To convert cleaned city-level air pollution data into a concise research brief that can support technical documentation, public communication, and stakeholder outreach.

## Dataset Overview
- City: {city}
- Date range: {s['min_date']} to {s['max_date']}
- Daily records analyzed: {s['total_records']}
- Dominant AQI bucket: {s['dominant_aqi_bucket']}

## Methodology
The uploaded CSV was validated, cleaned, sorted by city and date, and analyzed using deterministic Python/Pandas workflows. Missing pollutant values were handled using city-wise median imputation where possible, with overall median as fallback. AQI anomalies were flagged using AQI greater than mean plus two standard deviations.

## Pollutant-wise Analysis
{pollution_lines}

## Key Findings
{findings_lines}

## Worst Pollution Days
{worst_lines}

## Public Health and Environmental Interpretation
Sustained high AQI values indicate periods where public communication, awareness campaigns, and targeted mitigation discussions are important. Pollutant trends can help identify whether particulate matter or gaseous pollutants deserve stronger attention in outreach material.

## Climate-Tech Intervention Possibility
The analysis can support before/after documentation for air quality interventions such as green buffers, filtration pilots, algae-based biofiltration observations, or awareness-driven behavioral changes. This software does not claim hardware implementation; it helps document evidence.

## Outreach Recommendation
Use the findings to prepare short public summaries, college awareness material, NGO collaboration notes, and stakeholder briefing messages focused on observed pollution patterns in {city}.

## Limitations
Findings depend on the completeness and accuracy of the uploaded dataset. Imputation is used only for pollutant gaps and does not replace real sensor observations.

## Conclusion
{city} shows measurable air quality patterns that can be transformed into research documentation and outreach material. AirLens helps connect raw pollution data with actionable communication workflows.
"""
    return {"title": title, "executive_summary": executive, "key_findings": key_findings, "markdown_report": markdown}

def escape_latex(text: str) -> str:
    repl={"\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#", "_": r"\_", "{": r"\{", "}": r"\}", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}"}
    for k,v in repl.items(): text=text.replace(k,v)
    return text

def build_latex_report(city: str) -> str:
    brief = build_research_brief(city)
    body = escape_latex(brief["markdown_report"].replace("# ", "").replace("## ", "\n\\section*{"))
    # simple, safe LaTeX source
    return f"""\\documentclass[11pt]{{article}}
\\usepackage[margin=1in]{{geometry}}
\\usepackage{{hyperref}}
\\title{{{escape_latex(brief['title'])}}}
\\author{{AirLens}}
\\date{{}}
\\begin{{document}}
\\maketitle
\\begin{{verbatim}}
{brief['markdown_report']}
\\end{{verbatim}}
\\end{{document}}
"""
