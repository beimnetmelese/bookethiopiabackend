from .serializer import GetHotelSerializer,CreateHotelSerializer
from rest_framework.viewsets import ModelViewSet,GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .models import Hotel
from room.models import Room
from room.serializer import GetRoomSerializer

class HotelViewSet(ModelViewSet):
    queryset = Hotel.objects.all()
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_fields = ["city"]
    search_fields = ["name", "city"]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return GetHotelSerializer
        return CreateHotelSerializer
    
    def get_serializer_context(self):
        return  {"user_id": self.request.user.id}

class RoomRetrieveViewSet(RetrieveModelMixin,ListModelMixin,GenericViewSet):
    def get_queryset(self):
        return Room.objects.filter(hotel_id = self.kwargs["hotel_pk"])
    def get_serializer_class(self):
        return GetRoomSerializer

class HotelUserViewSet(ModelViewSet):
    def get_queryset(self):
        return Hotel.objects.filter(user_id = self.request.user.id)
    serializer_class = GetHotelSerializer

    
    
    
    
