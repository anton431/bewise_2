from django.urls import path

from .views import CreatePersonAPIView, AddAudioAPIView, download

urlpatterns = [
    path('create_user/', CreatePersonAPIView.as_view()),
    path('add_audio/', AddAudioAPIView.as_view()),
    path('record_id=<int:id>&user_id=<int:user_id>', download),
]