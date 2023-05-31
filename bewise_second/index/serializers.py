import os

from rest_framework import serializers
from .models import Person, Audio
from django.core.exceptions import ValidationError


class NameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('name',)

# class TokenSerializer(serializers.Serializer):
#     token = serializers.CharField(max_length=40)
#
#     def validate(self, data):
#         """
#         Проверка праильности токена
#         """
#         token_user = Person.objects.filter(pk=int(data['person']))
#         if data['token'] != token_user:
#             raise serializers.ValidationError("finish must occur after start")
#         return data


class AudioSerializer(serializers.ModelSerializer):
    # def validate(self, value):
    #     token_user = Person.objects.filter(pk=int(value['person']))
    #     if value['token'] != token_user:
    #         raise serializers.ValidationError("Not valid")
    #     return value

    token = serializers.CharField(max_length=40)
    class Meta:
        model = Audio
        fields = ('audio', 'person', 'token')




