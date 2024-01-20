from django.contrib import admin
from .models import Events, Transactions


@admin.register(Events)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'event',
        'user',
        'user_receiver',
        'session_key',
        'object',
        'event_date'
    )
    search_fields = ['event', 'user']
    list_filter = ('event',)


@admin.register(Transactions)
class TransactionsAdmin(admin.ModelAdmin):
    list_display = (
        'event',
        'object',
        'user',
        'number',
        'transaction_date',
    )
    search_fields = ['object', 'user']
    list_filter = ('transaction_date',)
