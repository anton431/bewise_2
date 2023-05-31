from django.contrib import admin
from django.urls import path

from .views import CreatePersonAPIView, AddAudioAPIView, download

urlpatterns = [
    path('create_user/', CreatePersonAPIView.as_view()),
    path('add_audio/', AddAudioAPIView.as_view()),
    path(r'record_id=<int:id>&user_id=<int:user_id>', download),
]

# http://localhost:8000/record?id=39&user=1