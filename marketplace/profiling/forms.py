from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField

from .models import User


class UserLoginForm(AuthenticationForm):
    username = UsernameField(
        label="",
        widget=forms.TextInput(attrs={
            "autofocus": True,
            "class": "form-control",
            "placeholder": "username",
        })
    )
    password = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={
            "autocomplete": "current-password",
            "class": "form-control",
            "placeholder": "password",
        }),
    )
    error_messages = {
        'invalid_login': ("Please enter a correct %(username)s and password."),
        'inactive': ("This account is inactive."),
    }

    class Meta:
        model = User
