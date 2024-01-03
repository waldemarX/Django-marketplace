from django.contrib import admin
from .models import Post, Categories


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'pub_date',
        'category',
        'is_published'
    )
    search_fields = ['title']
    list_editable = (
        'category',
        'is_published'
    )


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = (
        'category_name',
    )
    search_fields = ['category_name']