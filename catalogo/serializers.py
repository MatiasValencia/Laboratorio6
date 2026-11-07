from rest_framework import serializers
from .models import Automovil, Cliente

class AutomovilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Automovil
        fields = '__all__'


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'