# Generated by Django 4.2.5 on 2023-10-10 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0008_alter_recipe_tags_alter_recipestep_recipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='recipeunit',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
