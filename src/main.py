from fastapi import FastAPI, Depends, APIRouter
from auth.base_config import admin_only, protect_login, current_user
from auth.base_config import auth_backend, fastapi_users
from auth.schemas import UserRead, UserCreate
from auth.models import User
from tokens.tokens import generate_token, token_authentication



app = FastAPI(
    title="CFT-Test Task"
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    dependencies=[Depends(admin_only)],
    prefix="",
    tags=["Auth"],
)

@app.get("/token", dependencies=[Depends(current_user)], tags=["Generate"])
def get_token():
    return generate_token()

@app.get("/info/{username}", tags=["INFO"])
def get_information(token: str = Depends(token_authentication), user: User = Depends(current_user)):
    salary = user.salary
    promotion = user.promotion_date
    return {"Salary": salary, "promotion": promotion}