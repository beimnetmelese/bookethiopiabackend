from django.contrib import admin
from .models import Room

class RoomAdmin(admin.ModelAdmin):
    list_display = ["hotel", "title","size", "price"]

admin.site.register(Room,RoomAdmin)
