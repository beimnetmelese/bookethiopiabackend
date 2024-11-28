from .models import Booking
from .serializer import GetBookingSerializer, CreateBookingSerializer
from rest_framework.viewsets import ModelViewSet

class BookingViewSet(ModelViewSet):
    def get_queryset(self):
        return Booking.objects.filter(user_id = self.request.user.id)
    def get_serializer_class(self):
        if self.request.method == "GET":
            return GetBookingSerializer
        return CreateBookingSerializer
    def get_serializer_context(self):
        return {"user_id": self.request.user.id,
                "room_id": self.kwargs["room_pk"]}

class BookViewSet(ModelViewSet):
    def get_queryset(self):
        return Booking.objects.filter(user_id = self.request.user.id)
    def get_serializer_class(self):
        return GetBookingSerializer

class UnBookViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = GetBookingSerializer

class BookUserViewSet(ModelViewSet):
    def get_queryset(self):
        return Booking.objects.filter(room__hotel = self.kwargs["pk"])
    def get_serializer_class(self):
        return GetBookingSerializer
        
    
