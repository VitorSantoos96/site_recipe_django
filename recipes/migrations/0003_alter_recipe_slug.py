# Generated by Django 5.0.4 on 2024-05-21 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_rename_servings_time_recipe_servings_unit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
