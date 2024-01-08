from django import forms


from .models import Post


class ArticleCreationForm(forms.ModelForm):
    image = forms.ImageField()
    title = forms.CharField()
    text = forms.CharField()

    class Meta:
        model = Post
        fields = ("image", "title", "text")
        exclude = ('author', 'category')
