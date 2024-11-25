from CRUD.Users import get_users, create_user, delete_user, login, update_user,check_user_email
from Models.models import UserCreate,LoginDetails,UserUpdate
from fastapi import APIRouter

User_router = APIRouter()

x = 1 # replace with token value in the future
####################################################
@User_router.get("/api/users/")
async def get_users_t():
    if x == 1:
        return await get_users()
    return {'message':'Invalid token'}
####################################################
@User_router.post("/api/users/")
async def create_user_t(user: UserCreate):
    if x == 1:
        valid = await check_user_email(user.email)
        if valid == "false":
            return await create_user(user)
        return {"message":"email in use"}
    return {'message':'Invalid token'}
###################################################
@User_router.delete("/api/users/{user_id}")
async def delete_user_t(user_id: int):
    if x == 1:
        return await delete_user(user_id)
    return {'message':'Invalid token'}
###################################################
@User_router.post("/api/login/auth")
async def login_t(request: LoginDetails):
    if x == 1:
        return await login(request)
    return {'message':'Invalid token'}
###################################################
@User_router.patch("/api/users/")
async def update_user_t(user_update:UserUpdate):
    if x == 1:
        return await update_user(user_update)
    return {'message':'Invalid token'}
###################################################
