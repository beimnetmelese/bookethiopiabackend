from django.db import models
from hotel.models import Hotel
from room.models import Room
from user.models import User

class Booking(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete= models.CASCADE)
    date_booked = models.DateField()
    date_submitted = models.DateTimeField(auto_now_add=True)
