from pydantic import BaseModel
from typing import Optional

class UpdateLocationServiceConfigRequest(BaseModel):
    recognizer_key: Optional[str] = None
    resolver_key: Optional[str] = None
