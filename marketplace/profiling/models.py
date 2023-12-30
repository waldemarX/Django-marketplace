from django.db import models


class Author(models.Model):
    name = models.CharField('name', max_length=128)
    nickname = models.CharField('nickname', max_length=128, unique=True)
    items = models.ManyToManyField(
        "Item",
        blank=True,
        related_name="item",
        verbose_name="item"
    )

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return self.name


class Item(models.Model):
    title = models.CharField('title', max_length=128)
    description = models.TextField('description', blank=True, null=True)
    collection = models.CharField('collection', max_length=128, blank=True, null=True)
    # image = models.ImageField(upload_to="")
    creator = models.ForeignKey(
        "Author",
        on_delete=models.CASCADE,
        related_name="creator",
        verbose_name="creator"
    )
    owner = models.ForeignKey(
        "Author",
        on_delete=models.CASCADE,
        related_name="owner",
        verbose_name="owner"
    )
    price_eth = models.DecimalField('price_eth', default=0.000, max_digits=10, decimal_places=5)
    on_sale = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.title
