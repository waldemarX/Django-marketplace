from django.db import models
from profiling.models import Author


class Post(models.Model):
    title = models.CharField(max_length=256, verbose_name='Title')
    text = models.TextField(verbose_name='Text')
    highlighted_text = models.TextField(verbose_name='Highlighted Text', blank=True, null=True)
    is_published = models.BooleanField('Is published', default=True)
    image = models.ImageField(upload_to='post_image', default='post_image/default.jpg')
    pub_date = models.DateTimeField(
        verbose_name='Publishing date',
        auto_now_add=True
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        verbose_name='Article author'
    )
    category = models.ForeignKey(
        'Categories',
        on_delete=models.CASCADE,
        default=None,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.title


class Categories(models.Model):
    category_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name
