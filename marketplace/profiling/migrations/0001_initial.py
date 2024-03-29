# Generated by Django 3.2.16 on 2024-01-11 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('slug', models.CharField(max_length=128, verbose_name='slug')),
                ('banner', models.ImageField(default='collections/collection-default.jpg', upload_to='collection_banner')),
            ],
            options={
                'verbose_name': 'Collection',
                'verbose_name_plural': 'Collections',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=128, null=True, verbose_name='title')),
                ('image', models.ImageField(upload_to='item_image')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=4, verbose_name='price_eth')),
                ('on_sale', models.BooleanField(default=True)),
                ('likes', models.PositiveIntegerField(default=0, verbose_name='likes')),
                ('collection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='collection', to='profiling.collection', verbose_name='collection')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Items',
            },
        ),
    ]
