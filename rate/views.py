from rest_framework.viewsets import ModelViewSet
from .serializer import GetHotelRateSerializer,GetRoomRateSerializer,CreateHotelRateSerializer,CreateRoomRateSerializer
from .models import RoomRate,HotelRate

class RoomRateViewSet(ModelViewSet):
    def get_queryset(self):
        if self.request.method == "GET" or self.request.method == "POST":
            return RoomRate.objects.filter(room_id = self.kwargs["room_pk"])
        return RoomRate.objects.filter(user_id = self.request.user.id)
    
    def get_serializer_class(self):
        if self.request.method == "GET":
            return GetRoomRateSerializer
        return CreateRoomRateSerializer
    
    def get_serializer_context(self):
        return {"user_id": self.request.user.id,
                "room_id": self.kwargs["room_pk"]}

class HotelRateViewSet(ModelViewSet):
    def get_queryset(self):
        if self.request.method == "GET" or self.request.method == "POST":
            return HotelRate.objects.filter(hotel_id = self.kwargs["hotel_pk"])
        return HotelRate.objects.filter(user_id = self.request.user.id)
    
    def get_serializer_class(self):
        if self.request.method == "GET":
            return GetHotelRateSerializer
        return CreateHotelRateSerializer
    
    def get_serializer_context(self):
        return {"user_id": self.request.user.id,
                "hotel_id": self.kwargs["hotel_pk"]}
