from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from recipe.api import api as recipeAPI

from .admin import custom_admin_site

urlpatterns = [
    path('admin/', custom_admin_site.urls),
    path('recipe/', recipeAPI.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
