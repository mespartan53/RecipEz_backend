from ninja import FilterSchema, Field
from typing import Optional

class RecipeFilterSchema(FilterSchema):
    search: Optional[str] = Field(q=['title__icontains', 'tags__label__icontains', 'ingredients__ingredient__title__icontains'])
    # search: Optional[str] = Field(q=['title__icontains', 'ingredients_title__icontains', 'tags_label__icontains'])
