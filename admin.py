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


class CustomUserAdmin(admin.ModelAdmin):

    list_display = ('name', 'date', 'status')


    list_filter = ('status', 'category')


    search_fields = ('name', 'description')


    ordering = ('-date',)


    list_editable = ('status',)


    list_per_page = 10


    list_display = ('name', 'date_created', 'status')


    fieldsets = (
        (None, {
            'fields': ('name', 'description')
        }),
        ('Details', {
            'fields': ('status', 'category', 'date'),
        }),
    )

    # Валідація поля
    def clean_date(self):
        from django.core.exceptions import ValidationError
        if self.date > datetime.date.today():
            raise ValidationError("Дата не може бути в майбутньому!")
        return self.date


