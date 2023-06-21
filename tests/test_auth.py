import pytest
from sqlalchemy import insert, select

from auth.models import role, user
from conftest import client, async_session_maker


async def test_add_role():
    async with async_session_maker() as session:
        stmt = insert(role).values(id=1, name="user", permissions=None)
        await session.execute(stmt)
        await session.commit()
        stmtt = insert(role).values(id=2, name="admin", permissions=None)
        await session.execute(stmtt)
        await session.commit()

        query = select(role)
        result = await session.execute(query)
        assert result.all() == [(1, 'user', None), (2, 'admin', None)], "Роли не добавились"

def test_register():
    response = client.post("/register", json={
        "email": "string",
        "password": "string",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False,
        "username": "string",
        "role_id": 1
    })

    assert response.status_code == 401
    # Ошибка 401 так как регистрировать может только авторизованный админ