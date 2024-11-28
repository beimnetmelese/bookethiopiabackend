from django.db import models
from hotel.models import Hotel
from user.models import User

class Room(models.Model):
    user = models.ForeignKey(User,on_delete= models.CASCADE, related_name= "room" )
    hotel = models.ForeignKey(Hotel,on_delete= models.CASCADE, related_name= "room")
    title = models.CharField(max_length=255, null= True, blank=True)
    descriptions = models.TextField(null= True, blank=True)
    image = models.ImageField(upload_to= "room", null=False,blank=False)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    size = models.IntegerField(null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


