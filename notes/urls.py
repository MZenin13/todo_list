from django.urls import path, re_path, include

from .views import *

urlpatterns = [
    path('api/v1/notes/', NotesAPI_List.as_view()),
    path('api/v1/notes/<int:pk>/', NotesAPI_Retrieve.as_view()),
    path('api/v1/notecreate/', NotesAPI_Create.as_view()),
    path('api/v1/noteupdate/<int:pk>/', NotesAPI_Update.as_view()),
    path('api/v1/notedelete/<int:pk>/', NotesAPI_Delete.as_view()),
    path('api/v1/tags/', TagsAPI_List.as_view()),
    path('api/v1/tags/<int:pk>/', TagsAPI_RetrieveDelete.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.authtoken')),
]
