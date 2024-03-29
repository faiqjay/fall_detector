import uuid
import requests
from twilio.rest import Client
from fastapi.middleware.cors import CORSMiddleware

import private

from fastapi import FastAPI

from pydantic import BaseModel
from typing import List

from common.database import Database
from common.timezone import Date


class Device(BaseModel):
    _id: str
    Owner_name: str
    owner_email: str
    owner_emergency_contact: str


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
    date: str
    device_id: str
    latitude: str
    longitude: str
    status: str


class Panic(BaseModel):
    time: str
    date: str
    device_id: str
    latitude: str
    longitude: str
    status: str

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



Database.initialize()



'''
@app.get('/patients')
async def show_patients():
    # return db
    list_patients = []
    patients = Database.find("patient", {})
    for i in patients:
        list_patients.append(i)
    return list_patients


@app.get('/patients/{patient_id}')
async def show_patients_history(patient_id: str):
    # return db
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
    # db.append(new_pizza)
    Database.insert("patient", new_patient)
    return new_patient
'''

@app.get('/fall')
async def show_falls():
    # return db
    list_falls = []
    falls = Database.find("fall", {})
    for i in falls:
        list_falls.append(i)
    return list_falls


@app.get('/fall_device/{device_id}')
async def show_falls_device(device_id: str):
    # return db
    list_falls = []
    falls = Database.find("fall", {"device_id":device_id})
    for i in falls:
        list_falls.append(i)
    return list_falls

'''
@app.post('/fall')
async def register_fall(fall: Fall):
    new_fall = fall.dict()
    new_fall['_id'] = uuid.uuid4().hex
    print(new_fall)
    # db.append(new_pizza)
    Database.insert("fall", new_fall)
    return new_fall

#@app.post('/fall_post')
#async def register_fall(fall: Fall=Form(Fall)):
#    new_fall = fall.dict()
#    new_fall['_id'] = uuid.uuid4().hex
#    print(new_fall)
#    # db.append(new_pizza)
#    Database.insert("fall", new_fall)
#    return new_fall
'''

@app.get('/fall/{device_id}/{time}/{date}/{latitude}/{longitude}/{status}')
async def register_fall_get(device_id: str, time: str, date: str, latitude: str, longitude: str, status: str):

    date = Date.date()
    _id = uuid.uuid4().hex
    Database.insert("fall", {"_id": _id, "device_id": device_id, "time": time, "date": date, "latitude": latitude,
                             "longitude": longitude, "status": status})
    #patient = Database.find_one("patient", {"device_id": device_id})
    response_1 = requests.post('https://e-monitoring.herokuapp.com/devices',
                             json={"device_id": device_id, "time": time, "date": date, "latitude": latitude,
                                   "longitude": longitude, "status": status
                                   })
    print("Status code: ", response_1.status_code)
    response = requests.get("https://e-monitoring.herokuapp.com/users/devices/"+device_id)
    data_full = response.json()
    print(response.json())
    patient = data_full[0]

    #patient = {"name": "Juwon", "emergency_contact_1": "+2348162937944", "emergency_contact_2": "+2348162937944"}

    account_sid = private.account_sid
    auth_token = private.auth_token
    client = Client(account_sid, auth_token)

    message1 = client.messages.create(
        messaging_service_sid='MG2b502309ae0dfa1c768a55dcb0d0d170',
        body="EMERGENCY ALERT FOR "+patient["username"]+" https://www.google.com/maps/?q="+latitude+","+longitude+" "+date,
        to=patient["emergencyNumber"]
    )

    message2 = client.messages.create(
        messaging_service_sid='MG2b502309ae0dfa1c768a55dcb0d0d170',
        body="EMERGENCY ALERT FOR " + patient[
            "username"] + " https://www.google.com/maps/?q=" + latitude + "," + longitude + " " + date,
        to=patient["hospitalNumber"]
    )

    print(message1.sid)
    print(message2.sid)
    return "success"

'''
@app.get('/panic')
async def show_panics():
    # return db
    list_panics = []
    panics = Database.find("panic", {})
    for i in panics:
        list_panics.append(i)
    return list_panics


@app.post('/panic')
async def register_panic(panic: Panic):
    new_panic = panic.dict()
    new_panic['_id'] = uuid.uuid4().hex
    print(new_panic)
    # db.append(new_pizza)
    Database.insert("panic", new_panic)
    return new_panic


@app.get('/panic/{device_id}/{time}/{date}/{latitude}/{longitude}/{status}')
async def register_panic_get(device_id: str, time: str, date: str, latitude: str, longitude: str, status: str):
    _id = uuid.uuid4().hex
    Database.insert("panic", {"_id": _id, "device_id": device_id, "time": time, "date": date, "latitude": latitude,
                             "longitude": longitude, "status": status})
    return "success"
    '''