from django.contrib import admin
from todos.models import Todo

# Register your models here.
@admin.register(Todo)
class TodoModel(admin.ModelAdmin):
    list_display = ('activity', 'reminder', 'completed', 'activity_datetime')
    list_filter = ('activity', 'reminder', 'completed', 'activity_datetime')
    search_fields = ('activity', 'reminder', 'completed', 'activity_datetime')
    ordering = ('activity_datetime',)
