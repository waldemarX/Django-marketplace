# Generated by Django 3.2.16 on 2024-01-08 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiling', '0003_alter_item_collection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='on_sale',
            field=models.BooleanField(default=True),
        ),
    ]
