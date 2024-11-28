from rest_framework.viewsets import ModelViewSet
from user.models import User
from .serializer import UserRoomBookCheckerSerializer, UserHotelBookCheckerSerializer

class UserRoomBookCheckerViewSet(ModelViewSet):
    def get_queryset(self):
        return User.objects.filter(id = self.request.user.id)
    serializer_class = UserRoomBookCheckerSerializer
    def get_serializer_context(self):
        return {"room_id": self.kwargs["id"]}

class UserHotelBookCheckerViewSet(ModelViewSet):
    def get_queryset(self):
        return User.objects.filter(id = self.request.user.id)
    serializer_class = UserHotelBookCheckerSerializer
    def get_serializer_context(self):
        return {"hotel_id": self.kwargs["id"]}