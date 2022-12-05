from django.contrib import admin
from django.utils.html import format_html
#MODELS
from .models import (
    Team
)
# Register your models here.
class TeamAdmin(admin.ModelAdmin):   
    def image_tag(self, obj):
        return format_html('<img src="{}" width=40px; />'.format(obj.photo.url))
    image_tag.short_description = 'Image'

    list_display = ['id', 'image_tag', 'first_name', 'last_name', 'designation']
    list_display_links = ['id', 'first_name']
    
admin.site.register(Team, TeamAdmin)

