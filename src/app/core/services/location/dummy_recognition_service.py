from typing import List
from app.core.services.location.base.recognition_service_base import IRecognitionService

class DummyLocationRecognitionService(IRecognitionService):
    def extract_message_location(self, text: str) -> str:
      return "برزة"

    def extract_event_location(self, messages: List[str]) -> str:
      # Replace this later with LLM or rule-based extractor
      return "Jableh, Syria"
