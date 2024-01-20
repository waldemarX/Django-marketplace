from django import forms


from .models import Post


class ArticleCreationForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Post
        fields = ("image", "title", "text")
        exclude = ('author', 'category')
