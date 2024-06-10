from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_user=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
    is_teamlead=models.BooleanField(default=False)
    is_intern=models.BooleanField(default=False)
    is_frontoffice=models.BooleanField(default=False)
    phone=models.CharField(max_length=100,null=True,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True)
   
