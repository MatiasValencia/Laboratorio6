from .models import Automovil
from .serializers import AutomovilSerializer
from rest_framework import viewsets

class AutomovilViewSet(viewsets.ModelViewSet):
    queryset = Automovil.objects.all()
    serializer_class = AutomovilSerializer