from django.contrib import admin
from .models import Task, Message

class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'due_date', 'priority', 'assigned_to']

class MessageAdmin(admin.ModelAdmin):
    list_display = ['task', 'sender', 'content', 'timestamp']

admin.site.register(Task, TaskAdmin)
admin.site.register(Message, MessageAdmin)
