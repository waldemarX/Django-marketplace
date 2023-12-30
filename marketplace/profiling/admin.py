from django.contrib import admin

from .models import Author, Item


# admin.site.register(Author)
# admin.site.register(Item)
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'nickname',
    )
    filter_horizontal = ('items',)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'collection',
        'creator',
        'owner',
        'price_eth',
        'on_sale'
    )
    ist_editable = (
        'title',
        'collection',
        'price_eth',
        'on_sale'
    )
    search_fields = (
        'title',
        'owner')
    list_filter = ('on_sale',)
    list_display_links = ('title',)
    # readonly_fields = ('date_started',)
