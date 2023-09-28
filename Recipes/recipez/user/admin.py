from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from recipez.admin import custom_admin_site

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', )

custom_admin_site.register(User, UserAdmin)


