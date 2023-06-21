from datetime import datetime, timedelta
from fastapi import HTTPException
import secrets

tokens_dict = {}


def generate_token():
    token = secrets.token_urlsafe(nbytes=None)
    expires_at = datetime.utcnow() + timedelta(minutes=30)
    tokens_dict[token] = expires_at
    return token


def token_authentication(token: str):
    if token not in tokens_dict:
        raise HTTPException(status_code=401, detail="Invalid token")
    now = datetime.utcnow()
    if tokens_dict[token] < now:
        raise HTTPException(status_code=401, detail="Token expired")
    return token
