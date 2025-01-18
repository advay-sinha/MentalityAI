# mood_tracking/models.py

from django.db import models

class MoodLog(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    mood = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)  # New Field
    nationality = models.CharField(max_length=100, blank=True, null=True)  # New Field
    timestamp = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.name} - {self.mood} on {self.timestamp.strftime('%Y-%m-%d %H:%M')}"
