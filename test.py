# from pydantic import BaseModel
#teststest
# class Person(BaseModel):
#     name:str
#     age:int
# class Employee(Person):
#     employee_id:int
#     department:str
# emp= Employee(name="Sanil", age=18, employee_id=101, department="R&D")
# print(emp)



# data = {"name":"Sanil", "age":18, "employee_id":101, "department":"R&D"}
# User= Employee(**data)
# print(User)


# from pydantic import BaseModel, Field
# class Employee(BaseModel): 
#     name: str = Field(..., min_length=2, max_length=50, description="Employee full name") 
#     age: int = Field(..., gt=17, le=65, description="Age must be 18–65") 
#     salary: float = Field(..., gt=0, description="Monthly salary in USD") 
#     discount: float = Field(0.0, ge=0, le=100, description="Discount percentage 0–100")
# data=Employee(
#     name="Sanil",
#     age=18,
#     salary=155000
# )
# print(data)

# from pydantic import BaseModel, field_validator

# class Profile(BaseModel):
#     first_name: str
#     last_name: str

#     @field_validator("first_name", "last_name")
#     @classmethod
#     def capitalize_name(cls, value: str)->str:
#         return value.capitalize()
# profile=Profile(
#     first_name="Sanil",
#     last_name="Dagar"
# )
# print(profile)

# from pydantic import BaseModel, field_validator

# class User (BaseModel):
#     email:str

#     @field_validator("email")
#     @classmethod
#     def lower(cls, v: str)->str:
#         return v.lower()
# User(email="Said@GMAIL.COM").email

# email_id=User(
#     email="SAid@GMAIL.Com"
# )
# print(email_id)

# class Contact(BaseModel): 
#     email: str = Field(..., pattern=r"^[\w.*]+@[\w.*]+\.\w+$") 
#     phone: str = Field(..., pattern=r"^\+?\d{10,15}$")
# contact=Contact(
#     email="sanildagar@example.com",
#     phone="1234567890"
# )
# print(contact)

# from abc import ABC,abstractmethod
# class Vehicle(ABC):
#     @abstractmethod
#     def start_engine(self):
#         pass
#     @abstractmethod
#     def switch_off(self):
#         pass
#     def honk(self):
#         print(Beep! beep!)
            
# class Car(Vehicle):
# def start_engine



# from pydantic import BaseModel, computed_field
# class Product(BaseModel): 
#     price: float 
#     quantity: int 
#     @computed_field
#     @property 
#     def total_price(self)-> float: 
#         return self.price * self.quantity 
#     @computed_field 
#     @property
#     def total_quantity(self)-> int:
#         return self.quantity
# p = Product(price=100, quantity=3) 
# print(p.total_price)
# print(p.total_quantity)
# print(p.model_dump())

# from typing import Union, List 
# from pydantic import BaseModel 
# class TextContent(BaseModel):
#     type: str = "text" 
#     text: str 
# class ImageContent(BaseModel): 
#     type: str = "image" 
#     url: str 
#     alt: str 
# class Article(BaseModel): 
#     title: str 
#     blocks: List[Union[TextContent, ImageContent]]
# article = Article( 
#     title="My Post", 
#     blocks=[ 
#         {"type": "text", "text": "Hello world"}, 
#         {"type": "image", "url": "img.png", "alt": "a photo"}, 
#         ],
# )
# print(article)

from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
@app.get('/')
def home():
    return {"message":"I am working fine"}

class Data(BaseModel):
    id:int
    name:str

# @app.post('/')
# def save_data(data:Data):
#     print(data)
#     return "data found"

# users = {
#     1: {"name": "John"},
#     2: {"name": "Alice"}
# }

# @app.delete("/users/{id}")
# def delete_user(id: int):
#     if id in users:
#         del users[id]
#         return {
#             "message": "Deleted successfully",
#             "remaining_users": users
#         }

#     return {"message": "User not found"}

# users = [{
#     "id":1,
#     "name": "John",
#     "age":30,
#     "city":"new york"
# },
# {
#     "id": 2,
#     "name": "Alex",
#     "age":32,
#     "city":"london"
# }
# ]
# class data(BaseModel):
#     id:int
#     name:str
#     age:int
#     city:str

# @app.put('/update/{id}')
# def update_user(id:int,data:data):
#     print(id)
#     print(data)
#     return{
#         "message":"updated successfuly"
#     }





 
