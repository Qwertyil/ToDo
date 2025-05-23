from django.contrib import admin

from .models import Task, Theme


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_completed', 'creation_time', 'completion_time')
    list_filter = ('is_completed', 'creation_time')
    search_fields = ('title', 'additional')
    fields = ('title', 'additional', 'theme', 'creation_time', 'is_completed', 'completion_time')
    readonly_fields = ('creation_time', 'is_completed', 'completion_time')


admin.site.register(Task, TaskAdmin)
admin.site.register(Theme)
