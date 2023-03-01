from django.urls import path

from .views import *

urlpatterns = [
    path('api/v1/notelist/', NotesAPI_List.as_view()),
    path('api/v1/notelist/<int:pk>/', NotesAPI_Retrieve.as_view()),
    path('api/v1/notelist/<int:pk>/update/', NotesAPI_Update.as_view()),
    path('api/v1/notelist/<int:pk>/delete/', NotesAPI_Delete.as_view()),
    path('api/v1/notecreate/', NotesAPI_Create.as_view()),
]
