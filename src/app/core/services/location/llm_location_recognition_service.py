import json
import re
from typing import List
from app.core.configs.base_config import BaseConfig
import google.generativeai as genai
from app.core.services.location.base.recognition_service_base import IRecognitionService
from app.core.services.prompt.prompt_service import PromptService

class LLMLocationRecognitionService(IRecognitionService):
    def __init__(self, config: BaseConfig):
        try:
            genai.configure(api_key=config.get_api_key())
            self.model = genai.GenerativeModel("gemini-1.5-flash")
            self.prompt_service = PromptService()
        except Exception as e:
            raise RuntimeError(f"Failed to initialize Gemini model: {e}")

    def extract_message_location(self, text: str) -> str:
        try:
            key = "location_extraction"
            instructions = self.prompt_service.get_prompt_instructions(key)
            illustration = self.prompt_service.get_prompt_illustrations(key)
            format_spec = self.prompt_service.get_prompt_format(key)

            query = f"النص: {text}"
            full_prompt = f"{instructions}\n\n{illustration}\n\n{format_spec}\n\n{query}"

            response = self.model.generate_content(full_prompt)
            content = response.text.strip()

            # Remove Markdown-style code block fencing (e.g., ```json\n{...}\n```)
            content_cleaned = re.sub(r"```(?:json)?\n(.*?)\n```", r"\1", content, flags=re.DOTALL).strip()

            try:
                data = json.loads(content_cleaned)
                location = data.get("Location")
                if location:
                    return location
                return ""
            except json.JSONDecodeError:
                return content_cleaned

        except Exception as e:
            raise RuntimeError(f"LLM location extraction failed: {e}")

    def extract_event_location(self, messages: List[str]) -> str:
            # Replace this later with LLM or rule-based extractor
            return "Jableh, Syria"
