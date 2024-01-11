from django import forms
from .models import Item


class SingleItemCreationForm(forms.ModelForm):
    image = forms.ImageField()
    title = forms.CharField()
    price = forms.DecimalField()

    class Meta:
        model = Item
        fields = ("image", "title", "price")
        exclude = ('creator', 'owner',)


class SingleItemEditForm(forms.ModelForm):
    image = forms.ImageField()
    title = forms.CharField()
    price = forms.DecimalField()

    class Meta:
        model = Item
        fields = ("image", "title", "price")
        exclude = ('creator', 'owner',)
