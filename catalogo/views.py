from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response

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
]


@api_view(["GET"])
def api_root(request):
    return Response({
        "Listar Automóviles": reverse("listar_automoviles", request=request),
        "Crear Automóviles": reverse("crear_automovil", request=request),
    })


@api_view(["GET"])
def listar_automoviles(request):
    return Response(automoviles)


@api_view(["POST"])
def crear_automovil(request):
    nuevo_automovil = request.data.copy()
    nuevo_automovil["id"] = max(
        (automovil["id"] for automovil in automoviles),
        default=0,
    ) + 1
    automoviles.append(nuevo_automovil)
    return Response(nuevo_automovil, status=201)
