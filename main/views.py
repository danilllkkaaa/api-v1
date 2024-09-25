from rest_framework import generics, viewsets
from .MainSerializer import MainSerializer

from .models import Main


class MainViewSet(viewsets.ModelViewSet):
    queryset = Main.objects.all()
    serializer_class = MainSerializer
