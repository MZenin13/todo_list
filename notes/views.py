from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly

from .models import Note, Tag
from .permissions import IsOwnerOrAdmin
from .serializers import NoteViewSerializer, NoteUpdateSerializer, TagSerializer


""" Для заметок """
class NotesAPI_List(generics.ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteViewSerializer
    permission_classes = (AllowAny, )


class NotesAPI_Retrieve(generics.RetrieveAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteViewSerializer
    permission_classes = (AllowAny, )


class NotesAPI_Create(generics.CreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteUpdateSerializer
    permission_classes = (IsAuthenticated, )


class NotesAPI_Update(generics.RetrieveUpdateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteUpdateSerializer
    permission_classes = (IsOwnerOrAdmin, )


class NotesAPI_Delete(generics.DestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteUpdateSerializer
    permission_classes = (IsOwnerOrAdmin, )



""" Для тегов """
class TagsAPI_List(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class TagsAPI_RetrieveDelete(generics.RetrieveDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
