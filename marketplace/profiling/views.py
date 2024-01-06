from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import UserLoginForm
from django.contrib import auth

from .models import Item, User, Collection


def profile(request, author_username):
    template = "profiling/author.html"
    author_info = User.objects.get(nickname=author_username)
    item_info_owner = Item.objects.filter(owner=author_info.id)
    item_info_creator = Item.objects.filter(creator=author_info.id)
    context = {
        "author_info": author_info,
        "item_info_owner": item_info_owner,
        "item_info_creator": item_info_creator,
    }
    return render(request, template, context)


def collection(request, collection_slug):
    template = "profiling/collection.html"
    collection_info = Collection.objects.get(slug=collection_slug)
    collection_items = Item.objects.select_related("creator", "owner").filter(
        collection__slug=collection_slug
    )
    context = {
        "collection": collection_info,
        "items": collection_items,
        "dark": False,
    }
    return render(request, template, context)


def item(request, id):
    template = "profiling/item-details.html"
    item_info = Item.objects.select_related("owner").get(id=id)
    context = {
        "item_info": item_info,
    }
    return render(request, template, context)


def register(request):
    template = "profiling/register.html"
    context = {
        'dark': True,
        'subtitle': 'Sign in'
    }
    return render(request, template, context)


def login(request):
    template = "profiling/login.html"

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(request, username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {
        'form': form,
        'dark': True
    }
    return render(request, template, context)


def logout(request):
    template = "profiling/register.html"
    context = {
        ...
    }
    return render(request, template, context)
