# Generated by Django 3.2.16 on 2024-01-02 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_alter_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='highlighted_text',
            field=models.TextField(blank=True, null=True, verbose_name='Highlighted Text'),
        ),
    ]