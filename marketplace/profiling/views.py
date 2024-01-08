from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import SingleItemCreationForm, UserEditProfile, UserLoginForm, UserRegisterForm
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required

from .models import Item, User, Collection


def profile(request, author_username):
    template = "profiling/author.html"
    author_info = User.objects.get(username=author_username)
    item_info_owner = Item.objects.filter(owner=author_info.id)
    item_info_creator = Item.objects.filter(creator=author_info.id)
    context = {
        "author_info": author_info,
        "item_info_owner": item_info_owner,
        "item_info_creator": item_info_creator,
        "dark": False
    }
    return render(request, template, context)


@login_required
def edit_profile(request):
    template = "profiling/edit-profile.html"
    if request.method == "POST":
        form = UserEditProfile(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Changes successfully applied!")
            return HttpResponseRedirect(reverse("profiling:edit_profile"))
        else:
            errors = {
                "Username": request.POST["username"],
                "Email": request.POST["email"],
            }
            errors = [err[0] for err in errors.items() if not err[1]]
            messages.error(request, f"Please, do not leave required fields blank -> {', '.join(errors)}")
    else:
        form = UserEditProfile(instance=request.user)
    context = {
        'form': form,
        "dark": True,
        "subtitle": 'Edit Profile'

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


@login_required
def create_options(request):
    template = "profiling/create-options.html"
    context = {
        "dark": True,
        "subtitle": "Create Collectible"
    }
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
            messages.success(request, "Changes successfully applied!")
            return HttpResponseRedirect(reverse("profiling:create_single"))
        else:
            errors = {
                "Image": request.POST["image"],
                "Title": request.POST["title"],
                "Price": request.POST["price"]
            }
            errors = [err[0] for err in errors.items() if not err[1]]
            messages.error(request, f"Please, do not leave required fields blank -> {', '.join(errors)}")

    else:
        form = SingleItemCreationForm()

    context = {
        "dark": True,
        "subtitle": "Create Single Collectible"
    }
    return render(request, template, context)


def register(request):
    template = "profiling/register.html"
    if request.method == "POST":
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
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
            if user:
                auth.login(request, user)

                if request.POST.get('next', None):
                    return HttpResponseRedirect(request.POST.get('next'))
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
