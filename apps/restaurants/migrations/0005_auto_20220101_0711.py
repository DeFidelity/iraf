# Generated by Django 3.2.8 on 2022-01-01 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0004_food_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='food',
            options={'ordering': ['-date']},
        ),
        migrations.RenameField(
            model_name='restaurant',
            old_name='num_review',
            new_name='num_reviews',
        ),
        migrations.AddField(
            model_name='food',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]