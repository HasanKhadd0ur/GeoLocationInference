from typing import List
from camel_tools.ner import NERecognizer
from app.core.configs.base_config import BaseConfig
from app.core.services.location.base.recognition_service_base import IRecognitionService

class NERLocationRecognitionService(IRecognitionService):
    def __init__(self,config :BaseConfig):
        try:
            self.ner = NERecognizer.pretrained('CAMeL-Lab/bert-base-arabert')
        except Exception as e:
            raise RuntimeError(f"Failed to load CAMeL Tools NER model: {e}")

    def extract_message_location(self, text: str) -> List[str]:
        try:
            tokens = text.split()  # CAMeL expects a list of tokens
            tags = self.ner.predict_sentence(tokens)

            # Extract LOC entities
            locations = []
            current_entity = []
            for token, tag in zip(tokens, tags):
                if tag == 'B-LOC':
                    if current_entity:
                        locations.append(' '.join(current_entity))
                        current_entity = []
                    current_entity = [token]
                elif tag == 'I-LOC':
                    current_entity.append(token)
                else:
                    if current_entity:
                        locations.append(' '.join(current_entity))
                        current_entity = []
            if current_entity:
                locations.append(' '.join(current_entity))

            return locations[:1]  # Return only the first location found
        except Exception as e:
            raise RuntimeError(f"NER location extraction failed: {e}")
