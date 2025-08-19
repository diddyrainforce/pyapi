from pydantic import BaseModel
import os
from typing import List, Optional

class Config(BaseModel):
    PORT: int = int(os.getenv('PORT', '8080'))
    SUPABASE_URL: Optional[str] = os.getenv('SUPABASE_URL')
    SUPABASE_ANON_KEY: Optional[str] = os.getenv('SUPABASE_ANON_KEY')
    SUPABASE_SERVICE_ROLE_KEY: Optional[str] = os.getenv('SUPABASE_SERVICE_ROLE_KEY')
    OPENAI_API_KEY: Optional[str] = os.getenv('OPENAI_API_KEY')
    CORS_ORIGINS: List[str] = [o.strip() for o in os.getenv('CORS_ORIGINS', '').split(',') if o.strip()]

config = Config()
