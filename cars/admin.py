from django.contrib import admin

#MODELS
from .models import (
    Car
)
# Register your models here.

class CarAdmin(admin.ModelAdmin):
    list_display = ['id','car_title', 'year', 'price','body_style','fuel_type','state', 'is_featured']
    list_display_links = ['id', 'car_title']
    
    list_editable = ['is_featured']
    list_filter = ['is_featured', 'body_style']
    
admin.site.register(Car, CarAdmin)


