from django.db import models

class Carts(models.Model): 
    userid =  models.CharField(max_length=200) 
    productid = models.CharField(max_length=200) 
    created_at = models.DateField()
