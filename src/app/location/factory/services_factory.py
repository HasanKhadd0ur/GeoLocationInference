from app.core.configs.env_config import EnvConfig
from app.location.registry.resolution_service_registry import ServicesRegistry
from app.location.factory.location_service_config import LocationServiceConfigManager

config = EnvConfig()
config_manager = LocationServiceConfigManager()

def get_location_recognizer_service():
    key = config_manager.get_recognizer_key()
    return ServicesRegistry.get_location_recognizer(key, config)

def get_location_resolver_service():
    key = config_manager.get_resolver_key()
    return ServicesRegistry.get_location_resolver(key, config)

# from app.core.configs.env_config import EnvConfig
# from app.location.registry.resolution_service_registry import ServicesRegistry

# config = EnvConfig()
   
# def get_location_recognizer_service(key : str ):

#     return ServicesRegistry.get_location_recognizer(key,config)

# def get_location_resolver_service(key : str  ):
#     return ServicesRegistry.get_location_resolver(key, config)
