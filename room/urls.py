from rest_framework_nested import routers
from django.urls import path,include
from .views import RoomViewSet,GetSpecificRoomDateSizeViewSet
from rate.views import RoomRateViewSet

router = routers.DefaultRouter()
router.register("room", RoomViewSet, basename="room")

room_routers = routers.NestedDefaultRouter(router,"room", lookup = "room")
room_routers.register("rate", RoomRateViewSet, basename= "room_rate")

urlpatterns = [
    path("",include(router.urls)),
    path("", include(room_routers.urls)),
    path("book/<int:pk>/<str:date>/", GetSpecificRoomDateSizeViewSet.as_view({'get': 'list'}))
]