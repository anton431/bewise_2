from django.contrib import admin
from django.urls import path

from .views import CreatePersonAPIView

urlpatterns = [
    path('create_user/', CreatePersonAPIView.as_view()),
]