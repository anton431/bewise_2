from django.contrib import admin
from django.urls import path

from .views import CreatePersonAPIView, AddAudioAPIView

urlpatterns = [
    path('create_user/', CreatePersonAPIView.as_view()),
    path('add_audio/', AddAudioAPIView.as_view()),
]