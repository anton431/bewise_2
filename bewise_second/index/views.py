from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Person
from .serializers import NameSerializer


class CreatePersonAPIView(APIView):
    serializer_class = NameSerializer
    def post(self, request):
        name = request.data['name']
        my_serializer = NameSerializer(data=request.data)
        my_serializer.is_valid(raise_exception=True)
        person = Person.objects.create(name=name)
        return Response({'person_id': person.pk, 'token': person.token})