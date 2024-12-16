from django.shortcuts import render
from django.http import HttpResponse
import json
import uuid
import datetime
from users.models import Users

def registerUser(request):
    payload = json.load(request)
    userid = uuid.uuid4()

    # query = f"""insert into users(Name, userid, email, password, created_at) values ({payload.get('name')},{userid}, {payload.get('email')}, {payload.get('password')},{datetime.datetime.now()})"""
    payload['userid'] = userid
    payload['created_at'] = datetime.datetime.now()
    obj = Users(**payload)
    obj.save()

    return HttpResponse("user created successfully")


def login(request):
    payload = json.load(request)
    email = payload['email']
    password = payload['password']

    exist = Users.objects.filter(email=email, password=password) 
    if exist:
         return HttpResponse("success")

    

    return HttpResponse("invalid parameters")