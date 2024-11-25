from Utils.db import db
from Models.models import UserCreate,LoginDetails,UserUpdate


###############################################################
async def get_users():
    query = "SELECT * FROM users_main"
    rows = await db.fetch(query)
    return {"users": rows}

#################################################################
async def create_user(user: UserCreate):

    query = ("INSERT INTO users_main(name, email, password, role, createdOn) "
             "VALUES($1, $2, $3, $4, CURRENT_TIMESTAMP) "
             "RETURNING *;")

    row = await db.fetch(query, {user.name},{user.email},{user.password},{user.role})

    return {"message": "User created successfully", "user": row}

######################################################################
async def delete_user(user_id: int):
    await db.execute(
        "DELETE FROM users_main WHERE id = $1 RETURNING id", user_id
    )
    return {"message": "User has been deleted successfully."}
##########################################################################

async def login(request: LoginDetails):
    query = "SELECT * FROM users_main WHERE email=$1 AND password=$2"
    user = await db.fetch(query,{request.email},{request.password})
    if user:
        if user[0]['password'][0] == request.password:
            if user[0]['role'][0] == 'admin':
                return {"auth": "true","adminRights":"true","user":user[0]}
            else:
                return {"auth": "true","adminRights":"false","user":user[0]}
    return {"auth": "false"}
##########################################################################

async def update_user(user_update:UserUpdate):
    allowed_columns = ["name", "email", "password","role"]
    if user_update.element in allowed_columns:
        query = f"""
        UPDATE users_main
        SET {user_update.element} = $1
        WHERE id = $2
        """
        await db.fetch(query, {user_update.newValue}, user_update.id)
        return{"message":"Updated successfully"}
    return{"message":"Updated Unsuccessfully"}