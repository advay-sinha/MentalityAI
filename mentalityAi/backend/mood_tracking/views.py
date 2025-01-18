# mood_tracking/views.py

from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import MoodLog
from .forms import MoodLogForm

# Function to handle form submission
def submit_user_data(request):
    if request.method == 'POST':
        form = MoodLogForm(request.POST)

        if form.is_valid():
            form.save()  # Save the form data to the database
            return JsonResponse({'message': 'Data submitted successfully'})

        return JsonResponse({'error': 'Invalid form data'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
