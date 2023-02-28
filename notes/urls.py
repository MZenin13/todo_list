from django.urls import path

from .views import NotesView, NotesCreateUpdate

urlpatterns = [
    path('api/v1/notelist/', NotesView.as_view({'get': 'list'})),
    path('api/v1/notelist/<int:pk>/', NotesView.as_view({'get': 'retrieve'})),
    path('api/v1/notelist/<int:pk>/update/', NotesCreateUpdate.as_view({'get': 'retrieve', 'put': 'update'})),
    path('api/v1/notelist/<int:pk>/delete/', NotesCreateUpdate.as_view({'get': 'retrieve', 'delete': 'destroy'})),
    path('api/v1/notecreate/', NotesCreateUpdate.as_view({'post': 'create'})),
]
