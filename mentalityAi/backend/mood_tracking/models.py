# mood_tracking/models.py

from django.db import models

class MoodLog(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)  # Male/Female
    nationality = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.name} - {self.age} - {self.gender} - {self.nationality}"
