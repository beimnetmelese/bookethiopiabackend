from django.db import models
from hotel.models import Hotel
from user.models import User
from room.models import Room

class HotelRate(models.Model):
    RATE_CHOICES = [
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
        (6, "6"),
        (7, "7"),
        (8, "8"),
        (9, "9"),
        (10, "10"),
    ]
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete= models.CASCADE)
    rate = models.IntegerField(choices=RATE_CHOICES, null=False, blank=False)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class RoomRate(models.Model):
    RATE_CHOICES = [
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
        (6, "6"),
        (7, "7"),
        (8, "8"),
        (9, "9"),
        (10, "10"),
    ]
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    room = models.ForeignKey(Room, on_delete= models.CASCADE)
    rate = models.IntegerField(choices=RATE_CHOICES, null=False, blank=False)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

