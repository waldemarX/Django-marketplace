from django.db import models
from django.urls import reverse
from django.utils import timezone
import requests
from users.models import User


class Item(models.Model):
    title = models.CharField("title", max_length=128, blank=True, null=True)
    image = models.ImageField(upload_to="item_image")
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="creator",
        verbose_name="creator",
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="owner",
        verbose_name="owner"
    )
    collection = models.ForeignKey(
        "Collection",
        verbose_name="collection",
        related_name="collection",
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    price = models.DecimalField(
        "price_eth", default=0.00, max_digits=4, decimal_places=2
    )
    on_sale = models.BooleanField(default=True)
    likes = models.PositiveIntegerField(verbose_name="likes", default=0)
    creation_date = models.DateTimeField(
        verbose_name="creation date", auto_now_add=True,
    )

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"

    def price_in_usd(self):
        actual_price = requests.get(
            "https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD"
        ).json()["USD"]
        return f"{float(self.price) * actual_price:.2f}"

    def get_absolute_url(self):
        return reverse("profiling:item", args=[self.pk])

    def __str__(self):
        return self.title


class Collection(models.Model):
    title = models.CharField("title", max_length=128)
    description = models.TextField("description", blank=True, null=True)
    slug = models.CharField("slug", max_length=128)
    banner = models.ImageField(
        upload_to="collection_banner",
        default="collections/collection-default.jpg"
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="collection_creator",
        verbose_name="Collection creator",
    )

    class Meta:
        verbose_name = "Collection"
        verbose_name_plural = "Collections"

    def __str__(self):
        return self.title
