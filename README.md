# Laboratorio 6: API REST

Inicia el servidor de desarrollo con:

```powershell
python manage.py runserver
```

Abre `http://127.0.0.1:8000/` para acceder a la raíz de la API de Django REST
Framework y sigue el enlace `automoviles`.

La API navegable permite estas operaciones:

- `/automoviles/`: `GET` lista los automóviles y `POST` crea uno.
- `/automoviles/<id>/`: `GET` consulta un automóvil, `PUT` lo actualiza y
  `DELETE` lo elimina.

Los formularios para crear, actualizar y eliminar están disponibles en las
páginas de esos endpoints. Los campos del automóvil son `marca`, `modelo` y
`anio`.

El recurso `clientes` también está disponible como CRUD completo:

- `/clientes/`: `GET` lista los clientes y `POST` crea uno.
- `/clientes/<id>/`: `GET` consulta un cliente, `PUT` lo actualiza y
  `DELETE` lo elimina.

Los clientes de ejemplo del Laboratorio 6 se cargan mediante una migración y
se pueden administrar desde `/admin/`.

La comparación de líneas y la reflexión de este recurso están en
[EVIDENCIA.md](./EVIDENCIA.md).
