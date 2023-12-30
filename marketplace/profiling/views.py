from django.shortcuts import render
from .models import Item


def profile(request):
    template = 'profiling/author.html'
    return render(request, template)


def collection(request):
    template = 'profiling/collection.html'
    return render(request, template)


def item(request):
    template = 'profiling/item-details.html'
    item_info = Item.objects.all()[0]
    context = {
        'item_info': item_info,
    }
    return render(request, template, context)
