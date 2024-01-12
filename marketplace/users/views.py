from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from main.models import Events
from profiling.models import Item

from .forms import (
    UserEditProfile,
    UserLoginForm,
    UserRegisterForm,
)
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required

from .models import User
from profiling.utils import error_messages


def profile(request, author_username):
    template = "users/author.html"
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
    template = "users/edit-profile.html"
    if request.method == "POST":
        form = UserEditProfile(
            data=request.POST, instance=request.user, files=request.FILES
        )
        if form.is_valid():
            form.save()
            messages.success(request, "Changes successfully applied!")
            return HttpResponseRedirect(reverse("users:edit_profile"))
        else:
            error_messages(request, "username", "email")
    else:
        form = UserEditProfile(instance=request.user)
    context = {"form": form, "dark": True, "subtitle": "Edit Profile"}
    return render(request, template, context)


def register(request):
    template = "users/register.html"
    if request.method == "POST":
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance

            session_key = request.session.session_key

            auth.login(request, user)

            if session_key:
                Events.objects.filter(session_key=session_key).update(
                    user=user, session_key=None
                )

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
    template = "users/login.html"

    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(
                request, username=username, password=password
            )

            session_key = request.session.session_key

            if user:
                auth.login(request, user)

                if session_key:
                    Events.objects.filter(session_key=session_key).update(
                        user=user, session_key=None
                    )

                redirect_page = request.POST.get("next", None)
                if redirect_page and redirect_page != reverse(
                    "users:logout"
                ):
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
