from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Person, Audio
from .serializers import NameSerializer, AodioSerializer


class CreatePersonAPIView(APIView):
    serializer_class = NameSerializer
    def post(self, request):
        name = request.data['name']
        my_serializer = NameSerializer(data=request.data)
        my_serializer.is_valid(raise_exception=True)
        person = Person.objects.create(name=name)
        return Response({'person_id': person.pk, 'token': person.token})

class AddAudioAPIView(APIView):
    serializer_class = AodioSerializer
    def post(self, request):
        audio = request.data['audio']
        print(audio)
        person = request.data['person']
        serializer = AodioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        audiow = Audio.objects.create(audio=audio, person_id=person)
        return Response({'asd': audio})