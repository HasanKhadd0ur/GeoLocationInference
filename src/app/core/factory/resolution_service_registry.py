from typing import Type, Dict
from app.core.services.location.base.recognition_service_base import IRecognitionService
from app.core.services.location.base.resolution_service_base import IResolutionService

class ServicesRegistry:
    _recognizers: Dict[str, Type[IResolutionService]] = {}
    _resolvers: Dict[str, Type[IRecognitionService]] = {}

    @classmethod
    def register_location_recognizer(cls, name: str, service_cls: Type[IRecognitionService]):
        cls._recognizers[name] = service_cls

    @classmethod
    def register_location_resolver(cls, name: str, service_cls: Type[IResolutionService
                                                                     ]):
        cls._resolvers[name] = service_cls

    @classmethod
    def get_location_recognizer(cls, name: str, *args, **kwargs) -> IRecognitionService:
        if name not in cls._recognizers:
            raise ValueError(f"Location recognizer '{name}' not registered.")
        return cls._recognizers[name](*args, **kwargs)

    @classmethod
    def get_location_resolver(cls, name: str, *args, **kwargs) -> IResolutionService:
        if name not in cls._resolvers:
            raise ValueError(f"Location resolver '{name}' not registered.")
        return cls._resolvers[name](*args, **kwargs)
