from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'name', 'phone', 'cpf']
    search_fields = ['name', 'email', 'phone']
    list_per_page = 10
