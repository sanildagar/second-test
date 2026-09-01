from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
app = FastAPI()

users = []

# MODEL
class Data(BaseModel):
    id: int
    name: str
    age: int

class Data_Update(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None



# POST - Create User
@app.post("/users")
def create_user(data: Data):
    users.append(data)

    return {
        "data": data
    }


# GET - Get All Users
@app.get("/users")
def get_users():
    return users


# PUT - Update User
@app.put("/users/{id}")
def update_user(id: int, data: Data_Update):

    for user in users:
        if user.id == id:
            
            if data.name is not None:
                user.name = data.name

            if data.age is not None:
                user.age = data.age

            return {
                "message": "Updated successfully",
                "data": user
            }

    return {
        "message": "User not found"
    }


# DELETE - Delete User
@app.delete("/users/{id}")
def delete_user(id: int):

    for i, user in enumerate(users):
        if user.id == id:
            deleted_user = users.pop(i)

            return {
                "message": "Deleted successfully",
                "data": deleted_user,
                "remaining_users": users
            }

    return {
        "message": "User not found"
    }