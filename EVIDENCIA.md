# Evidencia: recurso Cliente

## Datos recuperados del Laboratorio 6

Los commits del repositorio original muestran que el recurso `Cliente` usa los
campos `nombre`, `correo` y `telefono`. Se conservaron los cuatro registros de
ejemplo que aparecen en la lista en memoria, incluidos los datos de Juan Perez
añadidos en [el commit de Gabriel](https://github.com/MatiasValencia/Laboratorio6/commit/356fcf49a3f29b74d4d9da6e04fe83d139442c2c).

## Comparación de líneas

| Implementación | Líneas de código |
|---|---:|
| CRUD equivalente con `ClienteList` y `ClienteDetail` (`APIView`) | 23 |
| `ClienteViewSet` (`ModelViewSet`) | 3 |

El conteo incluye definiciones y sentencias del CRUD; excluye imports, líneas en
blanco y el serializer/rutas, que son compartidos. Para `APIView` se contó la
implementación equivalente al patrón solicitado de las cinco operaciones y
`get_object()`; es un conteo reconstruido, porque el historial de esta rama no
contiene una versión de `Cliente` implementada con `APIView`. El `ViewSet`
actual solo necesita declarar la clase, `queryset` y `serializer_class`.

## Reflexión

`ModelViewSet` evita repetir la lógica estándar de listar, crear, consultar,
actualizar y borrar, por eso el CRUD queda más corto y uniforme. Preferiría
`APIView` cuando cada método necesite reglas o respuestas muy específicas, o
cuando el endpoint no corresponda al CRUD convencional de un modelo.
