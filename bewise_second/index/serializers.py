from rest_framework import serializers
from .models import Person, Audio


class NameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('name',)


class AudioSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=40)
    person_id = serializers.IntegerField()

    class Meta:
        model = Audio
        fields = ('audio', 'person_id', 'token')

