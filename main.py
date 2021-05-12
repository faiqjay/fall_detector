import uuid

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

class Fall(BaseModel):
    time: str
    device_id: str
    latlong: str
    status: str

class Panic(BaseModel):
    time: str
    device_id: str
    status: str


app = FastAPI()


Database.initialize()


@app.get('/')
async def index():
    return {"greeting": "welcome to Juwon's Pizza"}


@app.get('/patients')
async def show_patients():
    #return db
    list_patients = []
    patients = Database.find("patient", {})
    for i in patients:
        list_patients.append(i)
    return list_patients

@app.get('/patients/{patient_id}')
async def show_patients_history(patient_id: str):
    #return db
    list_patients = []
    patient = Database.find_one("patient", {"_id": patient_id})
    patients = Database.find("fall", {"device_id": patient['device_id']})
    for i in patients:
        list_patients.append(i)
    return list_patients

@app.post('/patients')
async def register_patient(patient: Patitient):
    new_patient = patient.dict()
    new_patient['_id'] = uuid.uuid4().hex
    print(new_patient)
    #db.append(new_pizza)
    Database.insert("patient", new_patient)
    return new_patient

@app.get('/fall')
async def show_falls():
    #return db
    list_falls = []
    falls = Database.find("fall", {})
    for i in falls:
        list_falls.append(i)
    return list_falls

@app.post('/fall')
async def register_fall(fall: Fall):
    new_fall = fall.dict()
    new_fall['_id'] = uuid.uuid4().hex
    print(new_fall)
    #db.append(new_pizza)
    Database.insert("fall", new_fall)
    return new_fall

@app.get('/fall/{device_id}/{time}/{latlong}/{status}')
async def register_fall_get(device_id: str, time: str, latlong: str, status: str):
    _id = uuid.uuid4().hex
    Database.insert("fall", {"_id": _id, "device_id": device_id, "time": time, "latlong": latlong, "status": status})
    return "success"
