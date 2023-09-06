from django.db import models
from django.contrib.auth.models import User,AbstractBaseUser,PermissionsMixin,BaseUserManager 

# Create your models here.


class Contact_details(models.Model):
    name = models.CharField(max_length=100)
    phone_no = models.IntegerField()
    email = models.EmailField()
    message = models.CharField(max_length=600)


class Subscribe_Option(models.Model):
    email = models.EmailField()