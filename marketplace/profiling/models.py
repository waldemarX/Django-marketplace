from django.db import models
import requests


class Author(models.Model):
    name = models.CharField("name", max_length=128)
    nickname = models.CharField("nickname", max_length=128, unique=True)
    avatar = models.ImageField(
        upload_to="author_avatar", default="author/author-default.jpg"
    )
    banner = models.ImageField(
        upload_to="author_banner", default="author_single/author_banner.jpg"
    )

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return self.name


class Item(models.Model):
    title = models.CharField("title", max_length=128, blank=True, null=True)
    image = models.ImageField(upload_to="item_image")
    creator = models.ForeignKey(
        "Author",
        on_delete=models.CASCADE,
        related_name="creator",
        verbose_name="creator",
    )
    owner = models.ForeignKey(
        "Author", on_delete=models.CASCADE,
        related_name="owner",
        verbose_name="owner"
    )
    collection = models.ForeignKey(
        "Collection",
        verbose_name="collection",
        related_name="collection",
        on_delete=models.CASCADE,
    )
    price = models.DecimalField(
        "price_eth", default=0.00, max_digits=4, decimal_places=2
    )
    on_sale = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"

    def __str__(self):
        return self.title

    def price_in_usd(self):
        actual_price = requests.get(
            "https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD"
        ).json()["USD"]
        return f"{float(self.price) * actual_price:.2f}"


class Collection(models.Model):
    title = models.CharField("title", max_length=128)
    description = models.TextField("description", blank=True, null=True)
    slug = models.CharField("slug", max_length=128)
    banner = models.ImageField(
        upload_to="collection_banner",
        default="collections/collection-default.jpg"
    )
    creator = models.ForeignKey(
        "Author",
        on_delete=models.CASCADE,
        related_name="collection_creator",
        verbose_name="Collection creator",
    )

    class Meta:
        verbose_name = "Collection"
        verbose_name_plural = "Collections"

    def __str__(self):
        return self.title
