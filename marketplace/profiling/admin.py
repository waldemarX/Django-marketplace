from django.contrib import admin

from .models import User, Item, Collection


class ItemTabAdmin(admin.TabularInline):
    model = Item
    fields = ("title", "collection", "price")
    search_fields = ("title", "collection")
    fk_name = "owner"
    extra = 1


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "first_name",
        "email",
        "last_login",
        "date_joined",
        "is_staff",
    )
    list_editable = ("is_staff",)
    search_fields = ["id", "username"]
    list_filter = ("date_joined", "last_login")

    inlines = (ItemTabAdmin,)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "collection",
        "creator",
        "owner",
        "price",
        "on_sale",
    )
    list_editable = ("price", "on_sale", "creator", "owner", "collection")
    search_fields = ["title"]
    list_filter = ("on_sale",)
    list_display_links = ("title",)


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ("title", "creator")
    list_editable = ("creator",)
    search_fields = ["title"]
    prepopulated_fields = {"slug": ("title",)}
