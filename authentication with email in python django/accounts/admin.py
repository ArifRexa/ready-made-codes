from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(CustomUser, UserAdmin)
class CustomAdminSite(admin.AdminSite):
    site_header = 'Authentication Administration'
    site_title = 'Authentication Center Admin'


