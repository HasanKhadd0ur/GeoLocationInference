from abc import ABC, abstractmethod

class IResolutionService(ABC):
    @abstractmethod
    def extract_event_location(self, text: str) -> str:
        pass

    @abstractmethod
    def geocode(self, location: str) -> dict:
        pass
