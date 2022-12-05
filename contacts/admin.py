from django.contrib import admin

#MODELS
from .models import (
    Contact
)
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'car_title']
    list_display_links = ['id', 'first_name']
    
admin.site.register(Contact, ContactAdmin)

