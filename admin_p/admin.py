from django.contrib import admin
from .models import UserDetails
# Register your models here.
class UserDetailAdmin(admin.ModelAdmin):
    list_display = ["name","mobile","email"]

admin.site.register(UserDetails, UserDetailAdmin)