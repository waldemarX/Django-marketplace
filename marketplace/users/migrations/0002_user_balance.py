# Generated by Django 3.2.16 on 2024-01-12 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4, verbose_name='balance'),
        ),
    ]
