# Generated by Django 3.2.8 on 2021-12-29 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_auto_20211229_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='about',
            field=models.CharField(max_length=255),
        ),
    ]
