from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import NoteTable

class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'text', 'created_at', 'updated_at')
    list_display_links = ('id', 'title')

admin.site.register(NoteTable, NoteAdmin)