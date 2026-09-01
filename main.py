from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
# @app.get("/")
# def heyyy():
#     return{"message":"server is up"}

users =[
    {"id":1,"name":"john","city":"fbd"},
    {"id":2,"name":"mary","city":"blb"},
    {"id":3,"name":"alex","city":"newyork"}
]

class Data(BaseModel):
    id:int
    name:str
    city:str

# @app.get("/users")
# def get_users():
#     print(users)
#     return{"data":users}



# @app.get("/users/{id}")
# def get_users(id:int):
#     print("recieved id:",id)
#     return{
#         "message":"user id recieved",
#         "id":id
#     }

# users=[]

# class Data(BaseModel):
#     id:int
#     name:str
#     cityyy:str

# @app.post("/users")
# def create_user(data:Data):
#     users.append(data)
#     return{
#         "message":"successfully done"
#     }

# @app.get("/users")
# def hey():
#     return users

   