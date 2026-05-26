def compare_intervention(city: str, pollutant: str, before_value: float, after_value: float, intervention_type: str):
    reduction = ((before_value - after_value) / before_value) * 100
    if reduction > 0:
        interpretation = "Positive reduction observed"
    elif reduction == 0:
        interpretation = "No measurable change observed"
    else:
        interpretation = "Pollutant value increased after observation"
    note = f"For {city}, {pollutant} changed from {before_value} to {after_value} after the documented {intervention_type}. This indicates a {round(reduction, 2)}% change. This module documents observations only and does not claim physical hardware operation."
    return {"reduction_percent": round(reduction, 2), "interpretation": interpretation, "observation_note": note}
