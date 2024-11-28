from rest_framework import serializers
from user.models import User
from .models import Hotel
from room.models import Room
from rate.models import RoomRate
from rate.models import HotelRate
from django.db.models.aggregates import Avg


class GetRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ["id","title","image", "price",  "rating",]
    
    
    rating = serializers.SerializerMethodField(method_name="rate")

    def rate(self,room:Room):
        rate = RoomRate.objects.filter(room_id = room.id).aggregate(avg = Avg("rate") )
        if rate["avg"] is None:
            return rate["avg"]
        return round(rate["avg"],1)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "profile","first_name", "last_name", "phone", "email"]

class CreateHotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ["id","name","image", "hotel_detail", "city","longitude","latitude", "date"]

    def create(self, validated_data):
        user_id = self.context["user_id"]
        return Hotel.objects.create(user_id = user_id, **validated_data)

class GetHotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ["id","user","name","image", "hotel_detail", "city","rating","longitude","latitude", "room","date"]
    
    user = UserSerializer()
    rating = serializers.SerializerMethodField(method_name= "rate")
    room = GetRoomSerializer(many = True)

    def rate(self, hotel:Hotel):
        rating = HotelRate.objects.filter(hotel_id = hotel.id).aggregate(avg = Avg("rate"))
        if rating["avg"] is None:
            return rating["avg"]
        return round(rating["avg"],1)
