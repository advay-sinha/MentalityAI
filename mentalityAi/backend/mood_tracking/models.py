# mood_tracking/models.py

from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    nationality = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.name} ({self.gender}, {self.age})"
