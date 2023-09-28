from django.contrib import admin
from .models import *
from recipez.admin import custom_admin_site

class RecipeStepInline(admin.TabularInline):
    model = RecipeStep
    extra = 1
    
class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1
    
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created')
    inlines = [RecipeStepInline, RecipeIngredientInline]

# Register your models here.
custom_admin_site.register(Tag)
custom_admin_site.register(RecipeUnit)
custom_admin_site.register(Ingredient)
custom_admin_site.register(Recipe, RecipeAdmin)
