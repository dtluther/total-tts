from django.shortcuts import render
from django.http import JsonResponse
from .models import TtsEntry

# Create your views here.
def avg_tts(request):
    """
    Return the average total_time_to_service
    """
    if request.method == 'GET':
        avg = TtsEntry.average_tts()
        return JsonResponse(avg)