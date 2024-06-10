from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_user = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_teamlead = models.BooleanField(default=False)
    is_intern = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_frontoffice = models.BooleanField(default=False)
    username = models.CharField(max_length=100, null=True,blank=True)
    password = models.CharField(max_length=100, null=True,blank=True)
