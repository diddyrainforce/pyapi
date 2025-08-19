from fastapi import Depends, HTTPException, Request
import httpx
from app.config import config

async def get_current_user(request: Request):
    auth_header = request.headers.get('Authorization', '')
    if not auth_header.startswith('Bearer '):
        raise HTTPException(status_code=401, detail='Missing token')
    token = auth_header[7:]
    if not config.SUPABASE_URL or not config.SUPABASE_ANON_KEY:
        raise HTTPException(status_code=500, detail='Supabase not configured')
    url = f"{config.SUPABASE_URL}/auth/v1/user"
    headers = {
        'Authorization': f'Bearer {token}',
        'apikey': config.SUPABASE_ANON_KEY,
    }
    async with httpx.AsyncClient(timeout=10) as client:
        resp = await client.get(url, headers=headers)
        if resp.status_code != 200:
            raise HTTPException(status_code=401, detail='Invalid token')
        return resp.json()
