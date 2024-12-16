from django.shortcuts import render
from django.http import HttpResponse
import json
import uuid
import datetime
from products.models import Products

def addProduct(request):
    payload = json.load(request)
    product_id = uuid.uuid4()
    payload['productid'] = product_id
    payload['created_at'] = datetime.datetime.now()
    obj = Products(**payload)
    obj.save()

    return HttpResponse("user created successfully")


def deleteProduct(request):
    payload = json.load(request)
    product_id = payload['productid']
    
    record = Products.objects.get(productid = product_id) 
    record.delete()
    if record:
        record.delete()
        return HttpResponse("delete successfully")


    return HttpResponse("not found")

def modifyProductDetails(request):
    payload = json.load(request)
    product_id = payload['product_id']


    update = Products.objects.filter(productid = product_id).update(**paylaod)
    
    return HttpResponse("update successfully")

def getAllProduct(request):
    
    records = list(Products.objects.all().iterator())
    json_res = []
    for record in records:
       
        print(dict(record.__dict__))
        json_res.append(record.__dict__)

    return HttpResponse({"data": json_res})