from .views import BookingViewSet, BookViewSet,BookUserViewSet,UnBookViewSet
from hotel.views import HotelViewSet
from room.views import RoomViewSet
from rest_framework_nested import routers
from django.urls import path,include

router = routers.DefaultRouter()
router.register("room", RoomViewSet, basename= "room")
router.register("book", BookViewSet, basename= "book")
router.register("unbook", UnBookViewSet, basename= "unbook")
room_router = routers.NestedDefaultRouter(router,"room", lookup = "room")
room_router.register("book", BookingViewSet, basename= "room")



urlpatterns = [
    path("", include(router.urls)),
    path("", include(room_router.urls)),
    path("bookuser/<int:pk>", BookUserViewSet.as_view({'get': 'list'}))


]