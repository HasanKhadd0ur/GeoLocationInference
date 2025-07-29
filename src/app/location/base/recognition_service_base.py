from abc import ABC, abstractmethod
from typing import List

from app.core.configs.base_config import BaseConfig

class IRecognitionService(ABC):
    def __init__(self,config :BaseConfig):
        self.config =config
    
    @abstractmethod
    def extract_message_location(self, text: str) -> str:
        pass
    
    @abstractmethod
    def extract_event_location(self, messages: List[str]) -> str:
        pass

