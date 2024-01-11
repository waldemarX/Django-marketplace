from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from main.models import Events

from .forms import (
    SingleItemCreationForm,
    SingleItemEditForm,
    UserEditProfile,
    UserLoginForm,
    UserRegisterForm,
)
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required

from .models import Item, User, Collection
from main.utils import check_if_like
from .utils import error_messages


def profile(request, author_username):
    template = "profiling/author.html"
    author_info = User.objects.get(username=author_username)
    item_info_owner = Item.objects.filter(owner=author_info.id)
    item_info_creator = Item.objects.filter(creator=author_info.id)
    context = {
        "author_info": author_info,
        "item_info_owner": item_info_owner,
        "item_info_creator": item_info_creator,
        "dark": False,
    }
    return render(request, template, context)


@login_required
def edit_profile(request):
    template = "profiling/edit-profile.html"
    if request.method == "POST":
        form = UserEditProfile(
            data=request.POST, instance=request.user, files=request.FILES
        )
        if form.is_valid():
            form.save()
            messages.success(request, "Changes successfully applied!")
            return HttpResponseRedirect(reverse("profiling:edit_profile"))
        else:
            error_messages(
                request,
                "username",
                "email"
            )
    else:
        form = UserEditProfile(instance=request.user)
    context = {"form": form, "dark": True, "subtitle": "Edit Profile"}
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
    is_like = check_if_like(request, item_info)
    context = {
        "item_info": item_info,
        'is_like': is_like,
        "dark": False
    }
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
            return HttpResponseRedirect(reverse("profiling:item", args=[item.id]))
        else:
            error_messages(
                request,
                "Image",
                "Title",
                "Price"
            )

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
        form = SingleItemEditForm(data=request.POST, instance=item, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Item successfully edited!")
            return redirect(request.META["HTTP_REFERER"])
            # return HttpResponseRedirect(reverse('profiling:edit_item', args=[item.id]))
        else:
            error_messages(
                request,
                "Title",
                "Price"
            )
    else:
        form = SingleItemEditForm()

    context = {"dark": True, 'item': item, "subtitle": "Edit Item"}
    return render(request, template, context)


@login_required
def delete_item(request, id):
    item = Item.objects.get(id=id)
    item.delete()
    return HttpResponseRedirect(reverse("profiling:profile", args=[request.user.username]))


def register(request):
    template = "profiling/register.html"
    if request.method == "POST":
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance

            session_key = request.session.session_key

            auth.login(request, user)

            if session_key:
                Events.objects.filter(session_key=session_key).update(user=user, session_key=None)

            return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserRegisterForm()

    context = {
        "form": form,
        "dark": True,
        "subtitle": "Sign in",
    }
    return render(request, template, context)


def login(request):
    template = "profiling/login.html"

    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(request, username=username, password=password)

            session_key = request.session.session_key

            if user:
                auth.login(request, user)

                if session_key:
                    Events.objects.filter(session_key=session_key).update(user=user, session_key=None)

                redirect_page = request.POST.get("next", None)
                if redirect_page and redirect_page != reverse('profiling:logout'):
                    return HttpResponseRedirect(request.POST.get("next"))
                else:
                    return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserLoginForm()

    context = {"form": form, "dark": True}
    return render(request, template, context)


@login_required
def logout(request):
    auth.logout(request)
    return redirect(reverse("main:index"))
