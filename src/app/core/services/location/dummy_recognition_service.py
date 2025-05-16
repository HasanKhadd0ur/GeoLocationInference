from app.core.services.location.base.recognition_service_base import IRecognitionService

class DummyLocationRecognitionService(IRecognitionService):
    def extract_message_location(self, text: str) -> str:
      return "برزة"