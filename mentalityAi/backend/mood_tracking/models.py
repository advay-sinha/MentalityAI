from django.db import models

class MoodLog(models.Model):
    name = models.CharField(max_length=100)   # Name of the person logging their mood
    age = models.IntegerField()                # Age of the person
    pmood = models.CharField(max_length=100)   # Mood description
    timestamp = models.DateTimeField(auto_now_add=True)  # Timestamp for when the mood was logged

    def __str__(self):
        return f"{self.name} - {self.pmood} on {self.timestamp.strftime('%Y-%m-%d %H:%M')}"
