# Generated by Django 3.2.16 on 2024-01-07 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiling', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='user_avatar/default.jpg', upload_to='user_avatar'),
        ),
        migrations.AlterField(
            model_name='user',
            name='banner',
            field=models.ImageField(default='user_banner/default.jpg', upload_to='user_banner'),
        ),
    ]