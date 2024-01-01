from django.db import models
import requests


class Author(models.Model):
    name = models.CharField('name', max_length=128)
    nickname = models.CharField('nickname', max_length=128, unique=True)
    avatar = models.ImageField(upload_to='author_avatar', blank=True, null=True)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return self.name


class Item(models.Model):
    title = models.CharField('title', max_length=128)
    description = models.TextField('description', blank=True, null=True)
    collection = models.CharField('collection', max_length=128, blank=True, null=True)
    image = models.ImageField(upload_to='item_image', blank=True, null=True)
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
    price = models.DecimalField('price_eth', default=0.00, max_digits=4, decimal_places=2)
    on_sale = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.title

    def price_in_dlr(self):
        actual_price = requests.get(
            'https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD'
            ).json()['USD']
        return f'{float(self.price) * actual_price:.2f}'
