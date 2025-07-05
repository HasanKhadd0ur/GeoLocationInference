from abc import ABC, abstractmethod

from app.core.models.location import Location

class IResolutionService(ABC):
    @abstractmethod
    def geocode(self, location: str) -> Location:
        pass
