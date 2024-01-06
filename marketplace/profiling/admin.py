from django.contrib import admin

from .models import User, Item, Collection


# admin.site.register(User)
# admin.site.register(Item)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    ...


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
        'creator'
    )
    list_editable = (
        'creator',
    )
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
