from django.contrib import admin

from .models import Author, Item, Collection


# admin.site.register(Author)
# admin.site.register(Item)
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'nickname',
    )
    list_display_links = ('name',)
    search_fields = ['name']


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'collection',
        'creator',
        'owner',
        'price',
        'on_sale'
    )
    list_editable = (
        'price',
        'on_sale',
        'creator',
        'owner',
    )
    search_fields = ['title']
    list_filter = ('on_sale',)
    list_display_links = ('title',)
    # readonly_fields = ('date_started',)


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
