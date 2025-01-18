from django.urls import path
from .views import MoodLogListCreateView

urlpatterns = [
    path('moodlogs/', MoodLogListCreateView.as_view(), name='mood-log-list-create'),  # API route for mood logs
]
