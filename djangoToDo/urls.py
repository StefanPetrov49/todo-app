from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('djangoToDo.todo_app.urls')),
    path('calendar/', include('djangoToDo.web_calendar.urls')),
]
