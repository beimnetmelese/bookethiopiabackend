from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    Sex = [
        ("M", "Male"),
        ("F", "Female"),
    ]
    profile = models.ImageField(upload_to="user",null=True, blank=True)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=1, choices=Sex, blank=True, null=True)
    phone = models.CharField(max_length=255,unique= True,null=True,blank=True)
    is_hotel_manager = models.BooleanField(default=False)


    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

