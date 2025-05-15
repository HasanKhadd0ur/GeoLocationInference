from app.core.configs.env_config import EnvConfig
from app.core.factory.resolution_service_registry import ServicesRegistry

config = EnvConfig()
   
def get_location_recognizer_service(key : str ):

    return ServicesRegistry.get_location_recognizer(key,config)

def get_location_resolver_service(key : str  ):
    return ServicesRegistry.get_location_resolver(key, config)
