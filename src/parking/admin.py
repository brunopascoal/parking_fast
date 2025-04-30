from django.contrib import admin

from .models import ParkingRecord, ParkingSpot


@admin.register(ParkingSpot)
class ParkingSpotAdmin(admin.ModelAdmin):
    list_display = ["__str__", "spot_number", "is_available"]
    search_fields = ["spot_number"]
    list_per_page = 10


@admin.register(ParkingRecord)
class ParkingRecordAdmin(admin.ModelAdmin):
    list_display = [
        "__str__",
        "vehicle",
        "parking_spot",
        "check_in_time",
        "check_out_time",
    ]
    search_fields = ["vehicle", "parking_spot"]
    list_per_page = 10
