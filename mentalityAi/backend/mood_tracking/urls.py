# mood_tracking/urls.py

from django.urls import path
from .views import submit_user_data

urlpatterns = [
    path('submit-data/', submit_user_data, name='submit-data'),
]
