from django.db import models

class Users(models.Model): 
    Name = models.CharField(max_length=200) 
    userid = models.CharField(max_length=200) 
    email = models.CharField(max_length=100) 
    password = models.CharField(max_length=100) 
    created_at = models.DateField()



