# Generated by Django 3.2.8 on 2022-04-07 22:42

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=300, primary_key=True, serialize=False, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('location', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('contact', models.CharField(max_length=255)),
                ('about', models.CharField(max_length=255)),
                ('rating', models.FloatField(blank=True, default=0.0, null=True)),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to='media/restaurants/', verbose_name='restaurant_image')),
                ('date', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('like', models.ManyToManyField(blank=True, related_name='_restaurants_restaurant_like_+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['rating'],
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('description', models.CharField(max_length=200, null=True)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('restaurant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='restaurantreview', to='restaurants.restaurant')),
                ('review_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['rating'],
            },
        ),
        migrations.AddField(
            model_name='restaurant',
            name='reviews',
            field=models.ManyToManyField(blank=True, related_name='reviews', to='restaurants.Review'),
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, max_length=300, unique=True)),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to='media/foods/', verbose_name='food_image')),
                ('price', models.PositiveSmallIntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('discount_price', models.PositiveSmallIntegerField()),
                ('star', models.FloatField(blank=True, default=0.0, null=True)),
                ('purchase', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('categories', models.ManyToManyField(blank=True, related_name='category', to='restaurants.FoodCategory')),
                ('restaurant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='restaurants', to='restaurants.restaurant')),
                ('try_it', models.ManyToManyField(blank=True, related_name='try_it', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
