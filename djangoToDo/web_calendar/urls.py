from django.urls import path

from djangoToDo.web_calendar.views import CalendarView

urlpatterns = (
    path('', CalendarView.as_view(), name='calendar'),
)
