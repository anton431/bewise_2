from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Person, Audio
from .serializers import NameSerializer, AudioSerializer
from django.core.exceptions import ValidationError
from os import path
from pydub import AudioSegment


class CreatePersonAPIView(APIView):
    serializer_class = NameSerializer
    def post(self, request):
        name = request.data['name']
        my_serializer = NameSerializer(data=request.data)
        my_serializer.is_valid(raise_exception=True)
        person = Person.objects.create(name=name)
        return Response({'person_id': person.pk, 'token': person.token})

class AddAudioAPIView(APIView):
    serializer_class = AudioSerializer
    def post(self, request):
        audio = request.data['audio']
        person = int(request.data['person'])
        token = request.data['token']
        token_user = Person.objects.filter(pk=person).first().token
        serializer = AudioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if str(token) != str(token_user):
            return Response(ValidationError('Неверный токен'))

        aud = Audio.objects.create(person_id=person, audio=audio)

        return Response({'URL': f'http://localhost:8000/record?id={aud.pk}&user={aud.person_id}'})