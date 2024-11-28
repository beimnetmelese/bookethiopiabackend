from django.contrib import admin
from .models import Hotel

class HotelAdmin(admin.ModelAdmin):
    list_display = ["name", "city"]

admin.site.register(Hotel, HotelAdmin)
