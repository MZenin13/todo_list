from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Note
from .serializers import ViewSerializer, UpdateSerializer


class NotesView(viewsets.ReadOnlyModelViewSet):
    queryset = Note.objects.all()
    serializer_class = ViewSerializer


class NotesCreateUpdate(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = UpdateSerializer
