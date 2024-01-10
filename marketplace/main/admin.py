from django.contrib import admin
from .models import Events


@admin.register(Events)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'event',
        'user',
        'object',
        'event_date'
    )
    search_fields = ['event', 'user']
    list_filter = ('event',)
