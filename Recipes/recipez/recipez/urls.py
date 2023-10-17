from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ninja import NinjaAPI
from ninja.security import APIKeyHeader

from recipe.api import recipeRouter
from user.api import userRouter
from .admin import custom_admin_site

class HeaderKey(APIKeyHeader):
    def authenticate(self, request, key):
        if key == 'secretkey':
            return key

header_key = HeaderKey()
api = NinjaAPI(csrf=True, auth=header_key)

api.add_router('recipez/', recipeRouter)
api.add_router('user/', userRouter)

urlpatterns = [
    path('admin/', custom_admin_site.urls),
    path('api/', api.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
