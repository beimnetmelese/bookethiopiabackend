from django.urls import path
from .views import UserRoomBookCheckerViewSet, UserHotelBookCheckerViewSet

urlpatterns = [
    path("is_hotel_rate_allowed/<int:id>/", UserHotelBookCheckerViewSet.as_view({'get': 'list'})),
    path("is_room_rate_allowed/<int:id>/", UserRoomBookCheckerViewSet.as_view({'get': 'list'})),
]