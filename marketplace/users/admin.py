from django.contrib import admin
from users.models import User

from profiling.admin import ItemTabAdmin


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
