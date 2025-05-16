from time import sleep
import requests
from app.core.configs.base_config import BaseConfig
from app.core.services.location.base.resolution_service_base import IResolutionService

class NominatimResolutionService(IResolutionService):
    def __init__(self, config: BaseConfig):
        self.config = config

    def extract_event_location(self, text: str) -> str:
        # Replace this later with LLM or rule-based extractor
        return "Jableh, Syria"

    def geocode(self, location: str) -> dict:
        try:
            url = self.config.get_geocoding_service_url()
            params = {
                "q": location,
                "format": "json",
                "limit": 1
            }
            headers = {
                "User-Agent": self.config.get_random_user_agent()
            }
            sleep(4)  # Simulate real-world delay or rate limiting
            response = requests.get(url, params=params, headers=headers)
            response.raise_for_status()
            results = response.json()

            if not results:
                return {"error": "Location not found"}

            result = results[0]
            return {
                "latitude": float(result["lat"]),
                "longitude": float(result["lon"])
            }

        except requests.RequestException as e:
            return {"error": str(e)}
