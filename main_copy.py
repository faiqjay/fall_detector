from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from common.database import Database


class Pizza(BaseModel):
    name: str
    toppings: List[str]


class Patitient(BaseModel):
    name: str
    _id: str
    device_id: str
    status: str


class Doctor(BaseModel):
    name: str
    _id: str
    status: str


class Admin(BaseModel):
    name: str
    _id: str
    status: str


app = FastAPI()

db = [
    {
        'id': 0,
        'name': 'text 1 pizza',
        'toppings': ['Mozarella cheese', 'Tomatoes', 'Basil']
    },
    {
        'id': 1,
        'name': 'text 2 pizza',
        'toppings': ['Mozarella cheese 2', 'Tomatoes 2', 'Basil 2']
    }
]

Database.initialize()


@app.get('/')
async def index():
    return {"greeting": "welcome to Juwon's Pizza"}


@app.get('/pizzas')
async def index():
    # return db
    list_ = []
    classes = Database.find("class", {})
    for i in classes:
        list_.append(i)
    return list_


@app.post('/pizzas')
async def post_pizza(pizza: Pizza):
    new_pizza = pizza.dict()
    new_pizza['id'] = db[-1]['id'] + 1
    print(new_pizza)
    db.append(new_pizza)
    return new_pizza


@app.get('/patients')
async def index():
    # return db
    list_patients = []
    patients = Database.find("patients", {})
    for i in patients:
        list_patients.append(i)
    return list_patients


@app.post('/pizzas')
async def post_pizza(pizza: Pizza):
    new_pizza = pizza.dict()
    new_pizza['id'] = db[-1]['id'] + 1
    print(new_pizza)
    db.append(new_pizza)
    return new_pizza