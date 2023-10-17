from django.db import models

class Tag(models.Model):
    label = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.label
    
class RecipeUnit(models.Model):
    label = models.CharField(max_length=20, null=False, unique=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.label
    
class Ingredient(models.Model):
    title = models.CharField(max_length=100, null=False, unique=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.title
    
class Recipe(models.Model):
    title = models.CharField(max_length=100, null=False)
    author = models.ForeignKey('user.User', on_delete=models.CASCADE, null=False)
    liked_by = models.ManyToManyField('user.User', related_name='liked_recipes')
    tags = models.ManyToManyField(Tag)
    isBeverage = models.BooleanField(default=False)
    servings = models.PositiveIntegerField(null=True)
    calories = models.PositiveIntegerField(null=True)
    notes = models.TextField(null=True)
    photo = models.ImageField(upload_to='recipe_photos/', null=True)
    created = models.DateTimeField(auto_created=True, null=True)
    
    def __str__(self) -> str:
        return self.title
    
class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    unit = models.ForeignKey(RecipeUnit, on_delete=models.PROTECT, null=True)
    amount = models.PositiveIntegerField(null = True)
    
class RecipeStep(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='directions')
    step_number = models.PositiveIntegerField(null=False)
    description = models.TextField(null=False)
    
    
    
    
    
