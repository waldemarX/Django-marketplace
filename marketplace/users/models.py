from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):
    avatar = models.ImageField(
        upload_to="user_avatar", default="user_avatar/default.jpg"
    )
    banner = models.ImageField(
        upload_to="user_banner", default="user_banner/default.jpg"
    )

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def get_absolute_url(self):
        return reverse("users:profile", args=[self.username])

    def __str__(self):
        return self.username
