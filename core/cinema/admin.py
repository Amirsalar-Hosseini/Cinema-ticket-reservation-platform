from django.contrib import admin
from .models import Location, Screen, Cinema


@admin.register(Cinema)
class CinemaAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'location', 'address', 'num_of_screens', 'total_capacity']


@admin.register(Screen)
class ScreenAdmin(admin.ModelAdmin):
    list_display = ['id', 'cinema', 'screen_number', 'capacity']


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['id', 'city', 'province']