from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),  # Включаем маршруты пользователей
    path('api/chat/', include('chat.urls')),    # Включаем маршруты чата
]
