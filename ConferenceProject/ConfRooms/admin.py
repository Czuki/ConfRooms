from django.contrib import admin

from .models import Room, Booking


class RoomAdmin(admin.ModelAdmin):
    list_display = ("name", "capacity", "projector")


class BookingAdmin(admin.ModelAdmin):
    list_display = ("date", "room", "comment")


admin.site.register(Room, RoomAdmin)
admin.site.register(Booking, BookingAdmin)


# Register your models here.
