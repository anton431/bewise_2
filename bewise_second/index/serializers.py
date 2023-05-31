import os

from rest_framework import serializers
from .models import Person, Audio
from django.core.exceptions import ValidationError


class NameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('name',)

class AodioSerializer(serializers.ModelSerializer):
    # token = serializers.CharField(source='person.token')
    class Meta:
        model = Audio
        fields = ('audio', 'person',)

