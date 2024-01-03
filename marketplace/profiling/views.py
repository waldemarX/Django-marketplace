from django.shortcuts import render
from .models import Item, Author


def profile(request, author_slug):
    template = 'profiling/author.html'
    author_info = Author.objects.get(nickname=author_slug)
    item_info_owner = Item.objects.filter(owner=author_info.id)
    item_info_creator = Item.objects.filter(creator=author_info.id)
    context = {
        'author_info': author_info,
        'item_info_owner': item_info_owner,
        'item_info_creator': item_info_creator,
    }
    return render(request, template, context)


def collection(request):
    template = 'profiling/collection.html'
    return render(request, template)


def item(request, id):
    template = 'profiling/item-details.html'
    item_info = Item.objects.select_related('owner').get(id=id)
    context = {
        'item_info': item_info,
    }
    return render(request, template, context)
