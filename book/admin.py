from django.contrib import admin
from .models import Booking

class BookAdmin(admin.ModelAdmin):
    list_display = ["user","room", "date_booked", "date_submitted"]

admin.site.register(Booking,BookAdmin)
