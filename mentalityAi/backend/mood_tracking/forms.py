# mood_tracking/forms.py

from django import forms
from .models import UserProfile

class MoodLogForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'age', 'gender', 'nationality']
