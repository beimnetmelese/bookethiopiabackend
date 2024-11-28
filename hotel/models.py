from django.db import models
from user.models import User

class Hotel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="hotel")
    name = models.CharField(max_length=255, null=False, blank=False)
    image = models.ImageField(upload_to="hotel", null=False,blank=False)
    hotel_detail = models.TextField()
    city = models.CharField(max_length=255, null=False,blank=False)
    longitude = models.FloatField(null=True,blank=True)
    latitude = models.FloatField(null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
