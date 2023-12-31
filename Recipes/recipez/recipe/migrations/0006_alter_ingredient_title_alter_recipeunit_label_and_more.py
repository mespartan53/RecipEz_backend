# Generated by Django 4.2.5 on 2023-09-28 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0005_recipe_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='recipeunit',
            name='label',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='label',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
