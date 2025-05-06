def recognize_locations(text: str, strategy: str = "llm"):
    # Stubbed logic for now
    if strategy == "llm":
        return {"locations": ["Aleppo", "Damascus"]}
    else:
        return {"locations": ["Unknown"]}
