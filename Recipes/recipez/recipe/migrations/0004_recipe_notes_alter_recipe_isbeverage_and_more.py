# Generated by Django 4.2.5 on 2023-09-28 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_recipe_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='notes',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='isBeverage',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(null=True, to='recipe.tag'),
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='amount',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='recipe.recipeunit'),
        ),
    ]
