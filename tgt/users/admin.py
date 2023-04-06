from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from .models import CustomUser, Department


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'middle_name', 'last_name', 'is_active')
    fields = ['username', 'password', 'email', 'first_name', 'middle_name', 'last_name', 'department', ('is_active',
              'is_superuser', 'is_staff'), ('phone_number_work', 'phone_number_mobile'), 'groups', 'user_permissions',
              ("last_login", "date_joined")]


class DepartmentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('department',)}


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Department, DepartmentAdmin)
