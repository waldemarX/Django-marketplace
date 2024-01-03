from django.contrib import admin
from .models import Post, Tags, Categories


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
    filter_horizontal = ('tags',)
    list_editable = (
        'category',
        'is_published'
    )


@admin.register(Tags)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        'tag_name',
    )
    search_fields = ['tag_name']


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = (
        'category_name',
    )
    search_fields = ['category_name']