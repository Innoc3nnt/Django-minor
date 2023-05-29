from django.contrib import admin
from .models import Pages

@admin.register(Pages)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'content']
    list_display_links = ['id']
    list_editable = ['name', 'content']
    search_fields = ['name', 'id']
    list_filter = ['name']
    list_per_page = 25