from rest_framework import generics

from .models import Note
from .serializers import ViewSerializer, UpdateSerializer


class NotesAPI_List(generics.ListAPIView):
    queryset = Note.objects.all()
    serializer_class = ViewSerializer


class NotesAPI_Retrieve(generics.RetrieveAPIView):
    queryset = Note.objects.all()
    serializer_class = ViewSerializer


class NotesAPI_Create(generics.CreateAPIView):
    queryset = Note.objects.all()
    serializer_class = UpdateSerializer


class NotesAPI_Update(generics.RetrieveUpdateAPIView):
    queryset = Note.objects.all()
    serializer_class = UpdateSerializer


class NotesAPI_Delete(generics.RetrieveDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = UpdateSerializer
