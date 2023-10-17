from django.db import Error
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from ninja import Router, Query
from typing import List

from .schema import *
from .models import *
from .filter import RecipeFilterSchema

recipeRouter = Router()

###           Tag API            ###
@recipeRouter.post('tag', response={200: TagSchema, 404: dict})
@login_required()
def create_tag(request, payload: TagSchema):
    if Tag.objects.filter(label__iexact=payload.label).exists():
        return 404, {'detail': 'Tag already exists with that name'}
    
    tag = Tag.objects.create(**payload.dict())
    return tag

@recipeRouter.get('tags', response=List[TagSchema])
def get_all_tags(request):
    tags = Tag.objects.all().order_by('label')
    return tags

@recipeRouter.get('tag/{int:tag_id}', response=TagSchema)
def get_tag_by_id(request, tag_id: int):
    tag = get_object_or_404(Tag, id=tag_id)
    return tag

@recipeRouter.get('tags/{str:tag_label}', response=List[TagSchema])
def get_tags_by_name(request, tag_label: str):
    tags = Tag.objects.filter(label__istartswith=tag_label).order_by('label').values()
    return tags


@recipeRouter.delete('tag/{int:tag_id}', response={200: dict, 404: dict})
@login_required()
def delete_tag_by_id(request, tag_id: int):
    tag = get_object_or_404(Tag, id=tag_id)
    tag.delete()
    return 200, {'success': True}
######################################

###           Recipe Unit API            ###
@recipeRouter.post('unit', response={200: RecipeUnitSchema, 404: dict})
@login_required()
def create_unit(request, payload: RecipeUnitSchema):
    if RecipeUnit.objects.filter(label__iexact=payload.label).exists():
        return 404, {'detail': 'Unit already exists with that label'}

    unit = RecipeUnit.objects.create(**payload.dict())
    return 200, unit

@recipeRouter.get('units', response={200: List[RecipeUnitSchema], 404: dict})
def get_all_units(request):
    try:
        units = RecipeUnit.objects.all().order_by(Lower('label'))
        return 200, units
    except:
        return 404, {'detail': 'Unable to find any units'}

@recipeRouter.get('unit/{int:unit_id}', response={200: RecipeUnitSchema, 404: dict})
def get_unit_by_id(request, unit_id: int):
    unit = get_object_or_404(RecipeUnit, id=unit_id)
    return 200, unit

@recipeRouter.get('units/{str:unit_str}', response={200: List[RecipeUnitSchema], 404: dict})
def get_units_by_str(request, unit_str: str):
    units = RecipeUnit.objects.filter(label__istartswith=unit_str).order_by('label').values()
    return 200, units

@recipeRouter.delete('unit/{int:unit_id}', response={200:dict, 404:dict})
@login_required()
def delete_unit_by_id(request, unit_id: int):
    unit = get_object_or_404(RecipeUnit, id=unit_id)
    unit.delete()
    return 200, {'success': True}
############################################

###           Ingredient API             ###
@recipeRouter.post('ingredient', response={200: IngredientSchema, 404: dict})
@login_required()
def create_ingredient(request, payload: IngredientSchema):
    if Ingredient.objects.filter(title__iexact=payload.title).exists():
        return 404, {'detail': 'An ingredient with that name already exists'}

    ingredient = Ingredient.objects.create(**payload.dict())
    return 200, ingredient

@recipeRouter.get('ingredients', response={200: List[IngredientSchema], 404: dict})
def get_all_ingredients(request):
    try:
        ingredients = Ingredient.objects.all().order_by('title')
        return 200, ingredients
    except:
        return 404, {'detail': 'Could not find any ingredients.'}

@recipeRouter.get('ingredient/{int:ingredient_id}', response={200: IngredientSchema, 404: dict})
def get_ingredient_by_id(request, ingredient_id: int):
    ingredient = get_object_or_404(Ingredient, id=ingredient_id)
    return ingredient

@recipeRouter.get('ingredients/{str:ingredient_str}', response={200: List[IngredientSchema], 404: dict})
def get_ingredient_by_name(request, ingredient_str: str):
    try:
        ingredients = Ingredient.objects.filter(title__istartswith=ingredient_str)
        return 200, ingredients
    except:
        return 404, {'detail': 'No ingredients found with that name'}

@recipeRouter.delete('ingredient/{int:ingredient_id}', response={200: dict, 404: dict})
@login_required()
def delete_ingredient(request, ingredient_id:int):
    ingredient = get_object_or_404(Ingredient, id=ingredient_id)
    ingredient.delete()
    return 200, {'success': True}
############################################

###           Recipe API                 ###
@recipeRouter.put('recipe/', response={200: RecipeSchema, 404: dict})
def update_recipe(request, payload: RecipeSchema):
    recipe = get_object_or_404(Recipe, id=payload.id)

    
    pass

@recipeRouter.post('recipe/', response={201: RecipeSchema, 404: dict})
@login_required()
def create_recipe(request, payload: RecipeSchemaIn):
    if Recipe.objects.filter(title__iexact=payload.title).exists():
        return 404, {'detail': 'Recipe already exists with that title'}

    #recipe = Recipe.objects.create(**payload.dict())
    author = get_object_or_404(User, id=payload.author.id)

    recipe = Recipe(
        title = payload.title,
        isBeverage = payload.isBeverage,
        author = author,
        servings = payload.servings,
        calories = payload.calories,
        notes = payload.notes
    )

    recipe.save()

    tags: List[Tag] = []
    for tag in payload.tags:
        recipe_tag, created = Tag.objects.get_or_create(label=tag.label)
        tags.append(recipe_tag)

    recipe.tags.set(tags)

    for direction in payload.directions:
        recipe_direction = RecipeStep(
            recipe = recipe,
            step_number = direction.step_number,
            description = direction.description
        )
        recipe_direction.save()

    for single_ingredient in payload.ingredients:
        ingredient_amount = single_ingredient.amount

        ingredient_unit, unit_created = RecipeUnit.objects.get_or_create(
            label=single_ingredient.unit.label
        )

        ingredient_title, ingredient_created = Ingredient.objects.get_or_create(
            title=single_ingredient.ingredient.title
        )

        recipe_ingredient = RecipeIngredient(
            recipe = recipe,
            ingredient = ingredient_title,
            unit = ingredient_unit,
            amount = ingredient_amount
        )

        recipe_ingredient.save()

    return 201, recipe

@recipeRouter.get('recipes/', response={200: List[RecipeSchema], 404: dict})
def get_all_recipes(request):
    try:
        recipe = Recipe.objects.all()
        return 200, recipe
    except:
        return 404, {'detail': 'Unable to retrieve any recipes'}

@recipeRouter.get('recipe/{int:recipe_id}', response={200: RecipeSchema, 404: dict})
def get_recipe_by_id(request, recipe_id: int):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return 200, recipe

@recipeRouter.get('recipe', response={200: List[RecipeSchema], 404: dict})
def get_recipe_by_filter(request, filters: RecipeFilterSchema=Query(...)):
    q = filters.get_filter_expression()
    recipes = Recipe.objects.filter(q).distinct()
    if recipes.exists():
        return recipes

    return 404, {'detail': 'No recipes found with that filter'}

@recipeRouter.delete('recipe/{int:recipe_id}', response={200: dict, 404: dict})
@login_required()
def delete_recipe_by_id(request, recipe_id:int):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.user == recipe.author:
        recipe.delete()
        return 200, {'detail': 'Successfully deleted recipe'}
    return 404, {'detail': 'Unable to delete recipe'}
############################################
