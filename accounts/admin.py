from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Додаткові поля', {'fields': ('phone_number', 'birth_date', 'profile_picture')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Додаткові поля', {'fields': ('phone_number', 'birth_date', 'profile_picture')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)