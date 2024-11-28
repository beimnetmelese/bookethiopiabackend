from .models import RoomRate, HotelRate
from rest_framework import serializers
from hotel.serializer import UserSerializer
from room.serializer import HotelSerializer
from room.models import Room



class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ["id","title", "size", "price"]

class GetRoomRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomRate
        fields = ["id", "user", "room", "rate", "comment", "date" ]
    
    user = UserSerializer()
    room = RoomSerializer()

class CreateRoomRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomRate
        fields = ["id", "rate", "comment", "date" ]
    
    def create(self, validated_data):
        user_id = self.context["user_id"]
        room_id = self.context["room_id"]
        return RoomRate.objects.create(user_id = user_id, room_id = room_id, **validated_data)
    
class GetHotelRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRate
        fields = ["id", "user", "hotel", "rate", "comment", "date" ]
    
    user = UserSerializer()
    hotel = HotelSerializer()

class CreateHotelRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRate
        fields = ["id", "rate", "comment", "date" ]
    
    def create(self, validated_data):
        user_id = self.context["user_id"]
        hotel_id = self.context["hotel_id"]
        return HotelRate.objects.create(user_id = user_id, hotel_id = hotel_id, **validated_data)
    
