from django.db import models
from profiling.models import User, Item


class Events(models.Model):
    event = models.CharField(verbose_name='event', max_length=50)
    event_date = models.DateTimeField(verbose_name="event date", auto_now_add=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user",
        verbose_name="user",
    )
    object = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name="object",
        verbose_name="object",
        blank=True
    )

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self):
        return self.event
