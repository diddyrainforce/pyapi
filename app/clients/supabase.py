from typing import Optional
from supabase import create_client, Client
from app.config import config

supabase_anon: Optional[Client] = None
supabase_admin: Optional[Client] = None

if config.SUPABASE_URL and config.SUPABASE_ANON_KEY:
    supabase_anon = create_client(config.SUPABASE_URL, config.SUPABASE_ANON_KEY)

if config.SUPABASE_URL and config.SUPABASE_SERVICE_ROLE_KEY:
    supabase_admin = create_client(config.SUPABASE_URL, config.SUPABASE_SERVICE_ROLE_KEY)
