# app/config/env_config.py
import os
import random
from typing import List

from dotenv import load_dotenv

from app.core.configs.base_config import BaseConfig

class EnvSettings:
    user_agents: List[str] = [
        "EventLocationService/1.0 (dummy1@example.com)",
        "EventLocationService/1.0 (dummy2@example.com)",
        "EventLocationService/1.0 (dummy3@example.com)",
        "EventLocationService/1.0 (dummy4@example.com)",
        "EventLocationService/1.0 (dummy5@example.com)",
        "EventLocationService/1.0 (dummy6@example.com)",
        "EventLocationService/1.0 (dummy7@example.com)",
        "EventLocationService/1.0 (dummy8@example.com)",
        "EventLocationService/1.0 (dummy9@example.com)",
        "EventLocationService/1.0 (dummy10@example.com)",
    ]

class EnvConfig(BaseConfig):
    def __init__(self):
        load_dotenv() 
        self.settings = EnvSettings()

    def get_user_agents(self) -> List[str]:
        return self.settings.user_agents

    def get_random_user_agent(self) -> str:
        return random.choice(self.settings.user_agents)
    def get_geocoding_service_url(self) -> str :
        return  "https://nominatim.openstreetmap.org/search"
    
    def get_api_key(self) -> str:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise EnvironmentError("LLM_API_KEY environment variable is not set")
        return api_key