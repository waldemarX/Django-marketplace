from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import (
    SingleItemCreationForm,
    SingleItemEditForm,
)
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Item, Collection
from main.utils import check_if_like
from .utils import error_messages


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
    is_like = check_if_like(request, item_info)
    context = {"item_info": item_info, "is_like": is_like, "dark": False}
    return render(request, template, context)


@login_required
def create_options(request):
    template = "profiling/create-options.html"
    context = {"dark": True, "subtitle": "Create Collectible"}
    return render(request, template, context)


@login_required
def create_single(request):
    template = "profiling/create-single.html"

    if request.method == "POST":
        form = SingleItemCreationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.creator = request.user
            item.owner = request.user
            item.save()
            messages.success(request, "Item successfully created!")
            return HttpResponseRedirect(
                reverse("profiling:item", args=[item.id])
            )
        else:
            error_messages(request, "Image", "Title", "Price")

    else:
        form = SingleItemCreationForm()

    context = {"dark": True, "subtitle": "Create Single Collectible"}
    return render(request, template, context)


@login_required
def edit_item(request, id):
    template = "profiling/edit-item.html"
    item = Item.objects.select_related("owner").get(id=id)

    if request.user != item.owner:
        messages.error(request, "You cannot change an item that is not yours.")
        return HttpResponseRedirect(reverse("main:index"))

    if request.method == "POST":
        form = SingleItemEditForm(
            data=request.POST, instance=item, files=request.FILES
        )
        if form.is_valid():
            form.save()
            messages.success(request, "Item successfully edited!")
            return redirect(request.META["HTTP_REFERER"])
        else:
            error_messages(request, "Title", "Price")
    else:
        form = SingleItemEditForm()

    context = {"dark": True, "item": item, "subtitle": "Edit Item"}
    return render(request, template, context)


@login_required
def delete_item(request, id):
    item = Item.objects.get(id=id)
    item.delete()
    return HttpResponseRedirect(
        reverse("users:profile", args=[request.user.username])
    )
