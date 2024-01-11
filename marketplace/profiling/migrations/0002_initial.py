# Generated by Django 3.2.16 on 2024-01-11 19:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiling', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to=settings.AUTH_USER_MODEL, verbose_name='creator'),
        ),
        migrations.AddField(
            model_name='item',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL, verbose_name='owner'),
        ),
        migrations.AddField(
            model_name='collection',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collection_creator', to=settings.AUTH_USER_MODEL, verbose_name='Collection creator'),
        ),
    ]
