from rest_framework import serializers
from .models import User
from django.db.models.aggregates import Count
from book.models import Booking
from rate.models import HotelRate, RoomRate
from room.serializer import HotelSerializer
from djoser.serializers import UserCreateSerializer

class RegisterUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ["id", "first_name", "last_name", "username","email", "sex","profile","phone", "password"] 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username", "email", "sex", "profile","phone","is_hotel_manager","hotel"]

        hotel = HotelSerializer()
class UserRoomBookCheckerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "isallowed1", "isallowed2"]
    
    isallowed1 = serializers.SerializerMethodField(method_name="is_room_rate_allowed")
    isallowed2 = serializers.SerializerMethodField(method_name="is_allowed2")

    def is_room_rate_allowed(self,user:User):
        room_id = self.context["room_id"]
        count = Booking.objects.filter(room_id = room_id).filter(user_id = user.id).aggregate(count = Count("id"))
        if (count["count"] == 0):
            allowed = False
        else:
            allowed = True
        return allowed
    def is_allowed2(self,user:User):
        room_id = self.context["room_id"]
        count = RoomRate.objects.filter(room_id = room_id).filter(user_id = user.id).aggregate(count = Count("id"))
        if (count["count"] == 0):
            allowed = True
        else:
            allowed = False
        return allowed

class UserHotelBookCheckerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "isallowed1", "isallowed2"]
    
    isallowed1 = serializers.SerializerMethodField(method_name="is_allowed")
    isallowed2 = serializers.SerializerMethodField(method_name="is_allowed2")

    def is_allowed(self,user:User):
        hotel_id = self.context["hotel_id"]
        count = Booking.objects.filter(hotel_id = hotel_id).filter(user_id = user.id).aggregate(count = Count("id"))
        if (count["count"] == 0):
            allowed = False
        else:
            allowed = True
        return allowed
    

    def is_allowed2(self,user:User):
        hotel_id = self.context["hotel_id"]
        count = HotelRate.objects.filter(hotel_id = hotel_id).filter(user_id = user.id).aggregate(count = Count("id"))
        if (count["count"] == 0):
            allowed = True
        else:
            allowed = False
        return allowed


