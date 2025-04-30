from django.contrib import admin
from .models import Vehicle, VehicleType

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'vehicle_type', 'owner', 'brand', 'model', 'plate', 'color']
    search_fields = ['plate', 'vehicle_type', 'owner']
    list_per_page = 10
    list_filter = ['vehicle_type', 'owner']
    
@admin.register(VehicleType)    
class VehicleTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name', 'description']
    list_per_page = 10