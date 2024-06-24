from django.contrib import admin
from notes.models import Note, Page


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    ...


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    ...