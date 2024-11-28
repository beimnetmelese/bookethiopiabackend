from django.contrib import admin
from .models import RoomRate,HotelRate

class HotelRateAdmin(admin.ModelAdmin):
    list_display = ["user", "hotel","rate"]

class RoomRateAdmin(admin.ModelAdmin):
    list_display = ["user", "room","rate"]

admin.site.register(HotelRate,HotelRateAdmin)
admin.site.register(RoomRate,RoomRateAdmin)