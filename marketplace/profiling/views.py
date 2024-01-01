from django.shortcuts import render
from .models import Item, Author


def profile(request, author_slug):
    template = 'profiling/author.html'
    author_info = Author.objects.get(nickname=author_slug)
    item_info = Item.objects.filter(owner=author_info.id)
    context = {
        'author_info': author_info,
        'item_info': item_info,
    }
    return render(request, template, context)


def collection(request):
    template = 'profiling/collection.html'
    return render(request, template)


def item(request, id):
    template = 'profiling/item-details.html'
    item_info = Item.objects.get(id=id)
    creator = Author.objects.get(id=item_info.creator.id)
    owner = Author.objects.get(id=item_info.owner.id)
    context = {
        'item_info': item_info,
        'creator': creator,
        'owner': owner
    }
    return render(request, template, context)
