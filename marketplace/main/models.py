from django.db import models
from profiling.models import Item
from users.models import User


class Events(models.Model):
    event = models.CharField(verbose_name="event", max_length=50)
    event_date = models.DateTimeField(
        verbose_name="event date", auto_now_add=True
    )
    session_key = models.CharField(
        verbose_name="session key", max_length=32, null=True, blank=True
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user",
        verbose_name="user",
        blank=True,
        null=True,
    )
    object = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name="object",
        verbose_name="object",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self):
        return self.event


class Transactions(models.Model):
    event = models.CharField(
        verbose_name="event", max_length=50, default="transaction"
    )
    object = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name="t_object",
        verbose_name="object",
        blank=True,
        null=True
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="t_user",
        verbose_name="user",
    )
    number = models.DecimalField(
        "eth", default=0.00, max_digits=4, decimal_places=2
    )
    transaction_date = models.DateTimeField(
        verbose_name="transaction date", auto_now_add=True
    )

    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"
