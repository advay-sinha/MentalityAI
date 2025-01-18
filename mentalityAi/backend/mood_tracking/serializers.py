from rest_framework import serializers
from .models import MoodLog

class MoodLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoodLog
        fields = ['id', 'name', 'age', 'pmood', 'timestamp']
