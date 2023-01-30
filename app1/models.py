from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class contact(models.Model):
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=100) 
    comments = models.CharField(max_length=1000)


class blogs(models.Model):
    usernamee = models.CharField(max_length=250)
    title = models.CharField(max_length=500,)
    description = models.CharField(max_length=1000)
    # ahmed
    

