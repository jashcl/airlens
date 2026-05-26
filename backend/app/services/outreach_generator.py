from .eda_service import get_city_summary

def generate_email(stakeholder, city: str):
    s = get_city_summary(city)
    subject = f"Air quality research and outreach collaboration for {city}"
    body = f"""Dear {stakeholder.name},

I am reaching out regarding a climate-tech research and outreach initiative focused on air quality communication in {city}.

Using a cleaned city-level air quality dataset, we observed an average AQI of {s['average_aqi']} across {s['total_records']} daily records, with the highest AQI reaching {s['max_aqi']} on {s['worst_day']['date']}. These insights can support awareness material, research documentation, and stakeholder discussions around practical air pollution communication.

Given {stakeholder.organization}'s work in {stakeholder.interest_area or 'environmental and community initiatives'}, I would be interested in exploring how this evidence can be converted into useful public-facing outreach.

Regards,
AirLens Research Workspace
"""
    return {"subject": subject, "email_body": body}
