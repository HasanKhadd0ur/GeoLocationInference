from abc import ABC, abstractmethod
from typing import List

from app.core.configs.base_config import BaseConfig

class IRecognitionService(ABC):
    def __init__(self,config :BaseConfig):
        super().__init__()
        self.config =config
    @abstractmethod
    def extract_message_location(self, text: str) -> List[str]:
        pass
