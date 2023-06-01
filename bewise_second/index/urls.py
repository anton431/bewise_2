from django.urls import path

from .views import CreatePersonAPIView, AddAudioAPIView, download

urlpatterns = [
    path('api/v1/create_user/', CreatePersonAPIView.as_view()),
    path('api/v1/add_audio/', AddAudioAPIView.as_view()),
    path('record_id=<int:id>&user_id=<int:user_id>', download),
]