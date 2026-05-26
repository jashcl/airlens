def classify_aqi(value: float) -> str:
    if value <= 50: return "Good"
    if value <= 100: return "Satisfactory"
    if value <= 200: return "Moderate"
    if value <= 300: return "Poor"
    if value <= 400: return "Very Poor"
    return "Severe"
