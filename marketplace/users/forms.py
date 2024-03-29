from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    UsernameField,
    UserCreationForm,
    UserChangeForm
)

from .models import User


class UserLoginForm(AuthenticationForm):
    username = UsernameField(
        label="",
    )
    password = forms.CharField(
        label="",
    )
    error_messages = {
        "invalid_login": ("Please enter a correct username and password."),
        "inactive": ("This account is inactive."),
    }

    class Meta:
        model = User


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(required=False)
    username = UsernameField()
    email = forms.CharField()

    class Meta:
        model = User
        fields = ("first_name", "username", "email", "password2")


class UserEditProfile(UserChangeForm):
    avatar = forms.ImageField(required=False)
    banner = forms.ImageField(required=False)
    first_name = forms.CharField(required=False)
    username = UsernameField()
    email = forms.CharField()

    class Meta:
        model = User
        fields = (
            'avatar',
            'banner',
            'first_name',
            'username',
            'email',
        )


class BalanceTopUpForm(forms.Form):
    balance = forms.DecimalField()

    class Meta:
        fields = ('balance',)

    def clean_balance(self):
        data = self.cleaned_data["balance"]

        if data <= 0:
            raise forms.ValidationError("Incorrect number")
        return data
