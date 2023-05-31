from rest_framework import serializers
from .models import Person


class NameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('name',)