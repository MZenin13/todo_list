from django.contrib import admin
from sqlparse.tokens import Token

from .models import Note, Tag


class NoteAdmin(admin.ModelAdmin):
    list_display = ('caption', 'reminder_time', 'tags')


admin.site.register(Note, NoteAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color')


admin.site.register(Tag, TagAdmin)

admin.site.register(Token)
