from rest_framework import serializers
from django.db.models.aggregates import Avg,Count
from .models import Room
from hotel.serializer import UserSerializer
from hotel.models import Hotel
from rate.models import RoomRate
from book.models import Booking

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ["id", "name", "city"]

class GetRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ["id","user", "hotel", "title", "descriptions","image", "price", "size", "rating","date"]
    
    user = UserSerializer()
    hotel = HotelSerializer()
    rating = serializers.SerializerMethodField(method_name="rate")

    def rate(self,room:Room):
        rate = RoomRate.objects.filter(room_id = room.id).aggregate(avg = Avg("rate") )
        if rate["avg"] is None:
            return rate["avg"]
        return round(rate["avg"],1)

class GetSpecificRoomDateSize(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ["id","room_size"]
    
    room_size = serializers.SerializerMethodField(method_name= "room_size_calculator")

    def room_size_calculator(self,room:Room):
        date = self.context["date"]
        sized = Booking.objects.filter(room_id = room.id).filter(date_booked = date).aggregate(count = Count("id"))
        size = room.size - sized["count"]
        return size



class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ["id","title", "image", "descriptions","price", "size", "date"]
    
    def create(self, validated_data):
        user_id = self.context["user_id"]
        hotel = Hotel.objects.get(user_id = user_id)
        return Room.objects.create(user_id = user_id, hotel = hotel, **validated_data)

