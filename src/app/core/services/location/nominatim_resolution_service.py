from time import sleep
import requests
from app.core.configs.base_config import BaseConfig
from app.core.factory.services_factory import get_location_recognizer_service
from app.core.models.location import Location
from app.core.services.location.base.resolution_service_base import IResolutionService


class NominatimResolutionService(IResolutionService):
    def __init__(self, config: BaseConfig):
        self.config = config

    def geocode(self, location: str) -> Location:
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
                # return {"error": "Location not found"}
                return Location()

            result = results[0]
            return Location( Latitude= float(result["lat"]) , Longitude=float(result["lon"]))
        except requests.RequestException as e:
            return {"error": str(e)}
