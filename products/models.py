from django.db import models

class Products(models.Model): 
    title = models.CharField(max_length=200) 
    productid = models.CharField(max_length=200) 
    company = models.CharField(max_length=100) 
    price = models.IntegerField()
    Category = models.CharField(max_length=100) 
    created_at = models.DateField()
