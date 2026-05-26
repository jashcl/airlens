from .eda_service import get_city_summary

def generate_content(city: str, content_type: str, audience: str, tone: str, topic: str | None = None):
    s = get_city_summary(city)
    base = f"{city} recorded an average AQI of {s['average_aqi']} between {s['min_date']} and {s['max_date']}, with a highest AQI of {s['max_aqi']} on {s['worst_day']['date']}."
    tags = ["air-quality", city.lower().replace(" ", "-"), "climate-tech", "aqi"]
    if content_type == "linkedin-post":
        title = f"Air quality insight: {city}"
        content = f"Air pollution data becomes more useful when it is communicated clearly.\n\n{base}\n\nThis kind of city-level analysis can support public awareness, research documentation, and stakeholder outreach for climate-tech initiatives.\n\n#AirQuality #ClimateTech #DataForGood"
    elif content_type == "awareness-points":
        title = f"Public awareness points for {city}"
        content = f"- Track AQI before outdoor activities.\n- Pay attention to high particulate matter days.\n- Use verified city-level air quality data when communicating risk.\n- {base}\n- Community outreach should focus on simple, evidence-based pollution communication."
    elif content_type == "stakeholder-note":
        title = f"Stakeholder briefing note — {city}"
        content = f"This note summarizes air quality observations for {city}. {base} The findings can support research discussions, community awareness activities, and possible climate-tech intervention documentation."
    else:
        title = f"Understanding air quality patterns in {city}"
        content = f"Air quality data can help turn environmental concern into practical communication. {base}\n\nFor a climate-tech team, these insights are useful because they connect pollutant trends with research briefs, public articles, and stakeholder outreach. The goal is not only to visualize AQI, but to explain what the numbers mean and where communication or intervention planning may be useful."
    return {"title": title, "content": content, "suggested_tags": tags}
