from django.contrib import admin

class CustomAdminSite(admin.AdminSite):
    site_header = 'RecipEz Admin'  
    site_title = 'RecipEz Admin'   
    index_title = 'RecipEz Dashboard'        

custom_admin_site = CustomAdminSite(name='customadmin')