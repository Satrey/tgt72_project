from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from .models import CustomUser, Department


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'middle_name', 'last_name', 'department', 'is_active')

    fieldsets = (
        ('Main', {'fields': ('username', 'email', 'password')}),
        ('Departament', {'fields': ('department',)}),
        ('Personal info', {'fields': ('avatar', 'first_name', 'middle_name', 'last_name')}),
        ('Contact info', {'fields': ('phone_number_work', 'phone_number_mobile')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        ('User registration', {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    search_fields = ('username', 'email',)
    ordering = ('username',)
    filter_horizontal = ()

    class Meta:
        model = CustomUser


class DepartmentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('department',)}


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Department, DepartmentAdmin)
