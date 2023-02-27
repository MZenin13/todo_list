from django.contrib import admin

from .models import Note, Tag


class NoteAdmin(admin.ModelAdmin):
    list_display = ('caption', 'reminder_time', 'get_tags')


admin.site.register(Note, NoteAdmin)


admin.site.register(Tag)
