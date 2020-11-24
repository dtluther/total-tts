from django.urls import path
from . import views

urlpatterns = [
    path('avg/', views.avg_tts)
]