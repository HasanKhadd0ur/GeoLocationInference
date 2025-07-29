from app.location.resolution.nominatim_resolution_service import NominatimResolutionService
from app.core.configs.env_config import EnvConfig
from app.core.models.location import Location

def test_geocode_known_location():
    service = NominatimResolutionService(EnvConfig())
    location = service.geocode("Berlin")
    assert isinstance(location, Location)
    assert location.latitude is not None
    assert location.longitude is not None

