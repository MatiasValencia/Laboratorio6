from .models import Automovil, Cliente
from .serializers import AutomovilSerializer, ClienteSerializer
from rest_framework import viewsets


class AutomovilViewSet(viewsets.ModelViewSet):
    queryset = Automovil.objects.all()
    serializer_class = AutomovilSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer