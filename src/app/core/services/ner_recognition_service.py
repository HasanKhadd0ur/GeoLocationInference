from typing import List
import stanza
from app.core.services.base.recognition_service_base import IRecognitionService
stanza.download('ar')

class NERLocationRecognitionService(IRecognitionService):
    def __init__(self) -> None:
        try:
            self.nlp = stanza.Pipeline(lang='ar', processors='tokenize,ner', use_gpu=False)
        except Exception as e:
            raise RuntimeError(f"Failed to load Stanza Arabic pipeline: {e}")

    def extract_message_location(self, text: str) -> List[str]:
        try:
            doc = self.nlp(text)
            locations = [ent.text for ent in doc.ents if ent.type == "LOC"]

            return locations[:1]  # Return only the first location found
        except Exception as e:
            raise RuntimeError(f"NER location extraction failed: {e}")
