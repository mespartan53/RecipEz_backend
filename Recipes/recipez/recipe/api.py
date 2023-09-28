from django.db import Error
from django.shortcuts import get_object_or_404
from ninja import NinjaAPI
from typing import List

from .schema import TagSchema
from .models import Tag

api = NinjaAPI()

###           Tag API            ###
@api.post('tag', response={200: TagSchema, 409: dict})
def create_tag(request, payload: TagSchema):
    if Tag.objects.filter(label__iexact=payload.label).exists():
        return 409, {'details': 'Tag already exists with that name'}
    
    tag = Tag.objects.create(**payload.dict())
    return tag

@api.get('tags', response=List[TagSchema])
def get_all_tags(request):
    tags = Tag.objects.all().order_by('label')
    return tags

@api.get('tag/{int:tag_id}', response=TagSchema)
def get_tag_by_id(request, tag_id: int):
    tag = get_object_or_404(Tag, id=tag_id)
    return tag

@api.get('tag/{str:tag_label}', response=List[TagSchema])
def get_tag_by_name(request, tag_label: str):
    tags = Tag.objects.filter(label__istartswith=tag_label).order_by('label').values()
    return tags



