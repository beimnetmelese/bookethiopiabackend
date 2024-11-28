from .models import Room
from datetime import datetime
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .filters import RoomFilter
from .serializer import GetRoomSerializer, CreateRoomSerializer,GetSpecificRoomDateSize
from rest_framework.viewsets import ModelViewSet

class RoomViewSet(ModelViewSet):
    queryset = Room.objects.all()
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_class = RoomFilter
    search_fields = ["title"]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return GetRoomSerializer
        return CreateRoomSerializer
    
    def get_serializer_context(self):
        return {"user_id": self.request.user.id}

class GetSpecificRoomDateSizeViewSet(ModelViewSet):
    def get_queryset(self):
        return Room.objects.filter(id = self.kwargs["pk"])
    serializer_class = GetSpecificRoomDateSize
    def get_serializer_context(self):
        string_date = self.kwargs["date"]
        date = datetime.strptime(string_date,"%Y-%m-%d").date()
        return {"date": date}