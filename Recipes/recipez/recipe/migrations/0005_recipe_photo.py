# Generated by Django 4.2.5 on 2023-09-28 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0004_recipe_notes_alter_recipe_isbeverage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='photo',
            field=models.ImageField(null=True, upload_to='recipe_photos/'),
        ),
    ]
