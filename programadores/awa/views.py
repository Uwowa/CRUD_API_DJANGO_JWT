from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from programadores.models import Programmer
from programadores.api.serializer import ProgrammerSerializer

class ProgrammerViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer
