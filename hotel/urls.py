from rest_framework_nested import routers
from django.urls import path,include
from . import views
from rate.views import HotelRateViewSet

router = routers.DefaultRouter()
router.register("hotel", views.HotelViewSet, basename= "hotel")
router.register("hoteluser", views.HotelUserViewSet, basename= "hoteluser")
hotel_router = routers.NestedDefaultRouter(router,"hotel", lookup = "hotel")
hotel_router.register("rate", HotelRateViewSet, basename= "hotel_name")
hotel_router.register("room", views.RoomRetrieveViewSet, basename="retrive_room")

urlpatterns = [
    path("",include(router.urls)),
    path("", include(hotel_router.urls))
]