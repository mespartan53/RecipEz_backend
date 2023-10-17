from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .models import User
from recipez.admin import custom_admin_site

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'nickname',)

class CustomGroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'permissions_list']

    def permissions_list(self, obj):
        return ", ".join([str(permission) for permission in obj.permissions.all()])
    permissions_list.short_description = 'Permissions'

custom_admin_site.register(User, UserAdmin)
custom_admin_site.register(Group, CustomGroupAdmin)
custom_admin_site.register


