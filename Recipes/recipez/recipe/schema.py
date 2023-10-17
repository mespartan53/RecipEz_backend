from typing import List
from datetime import date
from ninja import Schema, Field, ModelSchema
from ninja.orm import create_schema
from .models import *
from user.schemas import *

TagSchema = create_schema(Tag)
RecipeUnitSchema = create_schema(RecipeUnit)
IngredientSchema = create_schema(Ingredient)
RecipeIngredientSchema = create_schema(RecipeIngredient)
RecipeStepSchema = create_schema(RecipeStep)

class TagSchemaOut(Schema):
    label: str

class IngredientSchemaOut(Schema):
    title: str

class RecipeUnitSchemaOut(Schema):
    label: str

class RecipeStepSchemaOut(Schema):
    step_number: int
    description: str

class RecipeIngredientSchemaIn(ModelSchema):
    ingredient: IngredientSchemaOut
    unit: RecipeUnitSchemaOut
    class Config:
        model = RecipeIngredient
        model_fields = ['ingredient', 'unit', 'amount']

class RecipeIngredientSchemaOut(ModelSchema):
    ingredient: IngredientSchemaOut
    unit: RecipeUnitSchemaOut
    class Config:
        model = RecipeIngredient
        model_fields = ['recipe', 'ingredient', 'unit', 'amount']

class RecipeSchemaIn(ModelSchema):
    author: UserSchemaIn
    liked_by: List[UserSchemaOut] = []
    tags: List[TagSchemaOut] = []
    ingredients: List[RecipeIngredientSchemaIn]
    directions: List[RecipeStepSchemaOut]
    class Config:
        model = Recipe
        model_fields = '__all__'
        model_exclude = ['id', 'photo', 'created']

class RecipeSchema(ModelSchema):
    author: UserSchemaIn
    tags: List[TagSchemaOut] = []
    ingredients: List[RecipeIngredientSchemaOut]
    directions: List[RecipeStepSchemaOut]
    class Config:
        model = Recipe
        model_fields = '__all__'
    # id: int
    # title: str
    # author: UserSchemaOut
    # liked_by: List[UserSchemaOut] = None
    # tags: List[TagSchema] = None
    # isBeverage: bool = None
    # servings: int = None
    # calories: int = None
    # notes: str = None
    # photo: str = None
    # ingredients: List[RecipeIngredientSchema] = []
    # created: date
