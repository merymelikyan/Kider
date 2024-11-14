from django.contrib import admin
from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'cname', 'cage', 'content', 'timestamp')
    search_fields = ('name', 'email', 'cname', 'cage', 'content')
    list_filter = ('timestamp',)
