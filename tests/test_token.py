import pytest
from sqlalchemy import insert, select, String

from conftest import client, async_session_maker



def test_get_token():
    response = client.get("/token")
    assert response.status_code == 401
    #Ошибка авторизации, не авторизованный не может получить токен
def test_get_info():
    response = client.get("/info/{username}")
    assert response.status_code == 401
    #Ошибка авторизации, не авторизованный не может получить конфиденциальную информацию