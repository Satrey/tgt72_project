from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'task_start_date', 'task_crossroad_address', 'task_bug_description', 'task_sender',
                    'task_closed']
    list_filter = ['task_crossroad_address', 'task_bug_description', 'task_sender', 'task_start_date', 'task_closed']


admin.site.register(Task, TaskAdmin)
