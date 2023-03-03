import datetime
from typing import List

from django.shortcuts import get_object_or_404
from ninja import NinjaAPI, Schema

from .models import Note, Tag

api = NinjaAPI()


class TagIn(Schema):
    name: str
    color: str


class TagOut(Schema):
    id: int
    name: str
    color: str


class NoteIn(Schema):
    caption: str
    content: str
    reminder_time: datetime.datetime = None
    tag: list[int] = None


class NoteOut(Schema):
    id: int
    caption: str
    content: str
    reminder_time: datetime.datetime = None
    tag: list[TagOut] = None
    user_id: int


@api.get("/notes/{note_id}/", response=NoteOut)
def get_note(request, note_id: int):
    note = get_object_or_404(Note, id=note_id)
    return note


@api.get("/notes/", response=List[NoteOut])
def list_notes(request):
    qs = Note.objects.all()
    return qs


@api.post("/notes/")
def create_note(request, note_in: NoteIn):
    tags = Tag.objects.filter(id__in=note_in.tag)
    note = Note.objects.create(
        caption=note_in.caption, content=note_in.content,
        reminder_time=note_in.reminder_time, user_id=request.user.id
    )
    note.tag.set(tags)
    return {"success": True, "id": note.id}


@api.put("/notes/{note_id}")
def update_note(request, note_id: int, note_in: NoteIn):
    tags = Tag.objects.filter(id__in=note_in.tag)
    note = get_object_or_404(Note, id=note_id)
    for attr, value in note_in.dict().items():
        if attr == 'tag':
            note.tag.set(tags)
        else:
            setattr(note, attr, value)
    note.save()
    return {"success": True}


@api.delete("/notes/{note_id}")
def delete_note(request, note_id: int):
    note = get_object_or_404(Note, id=note_id)
    note.delete()
    return {"success": True}
