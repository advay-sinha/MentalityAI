from django.db import models

class MoodLog(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    pmood = models.CharField(max_length=100)  # For storing mood (e.g., happy, sad, etc.)
    timestamp = models.DateTimeField(auto_now_add=True)  # Automatically stores the time when the record is created

    def __str__(self):
        return f"{self.name} - {self.pmood} - {self.timestamp}"
