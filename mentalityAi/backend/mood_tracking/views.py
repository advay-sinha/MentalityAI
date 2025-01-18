from rest_framework import generics, permissions
from .models import MoodLog
from .serializers import MoodLogSerializer

class MoodLogListCreateView(generics.ListCreateAPIView):
    queryset = MoodLog.objects.all().order_by('-timestamp')  # List mood logs ordered by timestamp (latest first)
    serializer_class = MoodLogSerializer
    permission_classes = [permissions.AllowAny]  # Public access to the API (can be adjusted based on requirements)
