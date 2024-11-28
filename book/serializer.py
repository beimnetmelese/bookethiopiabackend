from rest_framework import serializers
from .models import Booking
from hotel.models import Hotel
from hotel.serializer import UserSerializer
from room.serializer import HotelSerializer
from room.models import Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ["id","title", "size", "hotel" ,"price"]
    hotel = HotelSerializer()

class GetBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["id", "user","room","date_booked", "date_submitted"]
    
    user = UserSerializer()
    room = RoomSerializer()

class CreateBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["id", "date_booked", "date_submitted"]
    
    def create(self, validated_data):
        user_id = self.context["user_id"]
        room_id = self.context["room_id"]
        hotel = Hotel.objects.get(room = room_id)
        return Booking.objects.create(user_id = user_id,room_id = room_id, hotel = hotel,**validated_data)