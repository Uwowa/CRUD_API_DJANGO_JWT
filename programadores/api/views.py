from rest_framework import viewsets
from programadores.models import Programmer
from programadores.api.serializer import ProgrammerSerializer

class ProgrammerViewSet(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer
