
class LocationController:

    @staticmethod
    def recognize_locations(text, strategy="llm"):
        if strategy == "spacy":
            return {"locations": text}
        return {"locations": text}

    @staticmethod
    def geocode_text(text):
        
        return {"coordinates": 122, "location": 1212}
