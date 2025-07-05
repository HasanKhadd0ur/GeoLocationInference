from typing import List
import stanza
from app.core.configs.base_config import BaseConfig
from app.core.services.location.base.recognition_service_base import IRecognitionService


class NERLocationRecognitionService(IRecognitionService):
    def __init__(self, config: BaseConfig):
        try:
            # Download only once
            stanza.download('ar', processors='tokenize,ner', verbose=False)
            self.nlp = stanza.Pipeline(lang='ar', processors='tokenize,ner', use_gpu=False)
        except Exception as e:
            raise RuntimeError(f"Failed to load Stanza NER pipeline: {e}")

    def extract_message_location(self, text: str) -> str:
        try:
            doc = self.nlp(text)
            locations = []

            for sentence in doc.sentences:
                for entity in sentence.ents:
                    if entity.type == 'LOC':
                        locations.append(entity.text)

            return  locations[:1]  if len(locations) > 0 else  "سوريا"  # Return only the first location
        except Exception as e:
            raise RuntimeError(f"NER location extraction failed: {e}")

    def extract_event_location(self, messages: List[str]) -> str:
        
        full_text = " ".join(
            msg.get("text") or msg.get("content") or "" for msg in messages
        )
        
        if not full_text.strip():
            return jsonify({"error": "No valid 'text' or 'content' found in messages"}), 400
   
        
        location_mention = self.extract_message_location(full_text)

        return  location_mention 
