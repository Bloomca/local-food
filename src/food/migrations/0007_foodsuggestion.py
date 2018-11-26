# Generated by Django 2.1.2 on 2018-11-26 02:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0006_auto_20181031_0602'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodSuggestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('original_name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('image_url', models.CharField(blank=True, max_length=300, validators=[django.core.validators.URLValidator()])),
                ('countries', models.CharField(max_length=200)),
            ],
        ),
    ]
