from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Automovil
from .serializers import AutomovilSerializer

automoviles = [
    {"id": 1, "marca": "Toyota", "modelo": "Corolla", "anio": 2022},
    {"id": 2, "marca": "Ford", "modelo": "Mustang", "anio": 2023},
    {"id": 3, "marca": "Honda", "modelo": "Civic", "anio": 2021},
    {"id": 4, "marca": "Mazda", "modelo": "CX-3", "anio": 2020},
    {"id": 5, "marca": "BMW", "modelo": "530i", "anio": 2006},
]

clientes = [
    {"id": 1, "nombre": "Ana Perez", "correo": "ana.perez@example.com", "telefono": "+56911111111"},
    {"id": 2, "nombre": "Luis Gonzalez", "correo": "luis.gonzalez@example.com", "telefono": "+56922222222"},
    {"id": 3, "nombre": "Camila Rojas", "correo": "camila.rojas@example.com", "telefono": "+56933333333"},
    {"id": 4, "nombre": "Juan Perez", "correo": "juan.perez@example.com", "telefono": "+56944444444"},
]

class AutomovilList(APIView):
    def get(self, request):
        return Response(AutomovilSerializer(Automovil.objects.all(), many=True).data)

    def post(self, request):
        serializer = AutomovilSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request, pk):
        serializer = AutomovilSerializer(self.get_object(pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(status=204)