from django.contrib import admin
from .models import Task

@admin.register(Task)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'task', 'num', 'current_date']
    list_display_links = ['task']
    list_editable = []
    search_fields = ['current_date']
    list_filter = ['task', 'num']
    list_per_page = 50