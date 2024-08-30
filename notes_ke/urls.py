from django.contrib import admin
from django.urls import path, include, re_path
from notes_app.views import NotesAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', include('notes_app.urls')),
    # API для авторизации
    path('api/v1/auth/', include('djoser.urls')),
    # API для получения токена
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    # API для получения всех заметок(GET) и добавления новой(POST)
    path('api/v1/notes/', NotesAPIView.as_view()),
]
