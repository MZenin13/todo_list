from django.urls import path

from .views import NotesAPIView


urlpatterns = [
    path('api/v1/notelist/', NotesAPIView.as_view()),
]
