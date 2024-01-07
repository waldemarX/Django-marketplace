from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    UsernameField,
    UserCreationForm,
)

from .models import User


class UserLoginForm(AuthenticationForm):
    username = UsernameField(
        label="",
    )
    password = forms.CharField(
        label="",
    )

    # username = UsernameField(
    #     label="",
    #     widget=forms.TextInput(attrs={
    #         "autofocus": True,
    #         "class": "form-control",
    #         "placeholder": "username",
    #     })
    # )
    # password = forms.CharField(
    #     label="",
    #     widget=forms.PasswordInput(attrs={
    #         "autocomplete": "current-password",
    #         "class": "form-control",
    #         "placeholder": "password",
    #     }),
    # )
    error_messages = {
        "invalid_login": ("Please enter a correct username and password."),
        "inactive": ("This account is inactive."),
    }

    class Meta:
        model = User


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField()
    username = UsernameField()
    email = forms.CharField()

    class Meta:
        model = User
        fields = ("first_name", "username", "email", "password2")
