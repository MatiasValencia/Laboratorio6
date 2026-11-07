from django.test import TestCase
from .models import Automovil, Cliente


class ApiRootTests(TestCase):
    def test_api_root_lists_automobile_endpoints(self):
        response = self.client.get("/", HTTP_ACCEPT="text/html")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "/automoviles/")
        self.assertContains(response, "/clientes/")


class AutomovilEndpointTests(TestCase):
    def test_get_lists_automoviles(self):
        response = self.client.get("/automoviles/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    def test_browsable_api_offers_create_form(self):
        response = self.client.get("/automoviles/", HTTP_ACCEPT="text/html")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "POST")
        for field in ("marca", "modelo", "anio"):
            self.assertContains(response, field)

    def test_browsable_api_creates_automovil_from_form_data(self):
        response = self.client.post(
            "/automoviles/",
            {"marca": "Toyota", "modelo": "Corolla", "anio": 2022},
            HTTP_ACCEPT="text/html",
        )

        self.assertEqual(response.status_code, 201)
        self.assertTrue(Automovil.objects.filter(marca="Toyota").exists())

    def test_browsable_api_offers_update_and_delete(self):
        automovil = Automovil.objects.create(marca="Toyota", modelo="Corolla", anio=2022)

        response = self.client.get(
            f"/automoviles/{automovil.pk}/",
            HTTP_ACCEPT="text/html",
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "PUT")
        self.assertContains(response, "DELETE")

    def test_post_creates_automovil(self):
        response = self.client.post(
            "/automoviles/",
            {"marca": "Toyota", "modelo": "Corolla", "anio": 2022},
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Automovil.objects.count(), 1)

    def test_put_updates_automovil(self):
        automovil = Automovil.objects.create(marca="Toyota", modelo="Corolla", anio=2022)

        response = self.client.put(
            f"/automoviles/{automovil.pk}/",
            {"marca": "Honda", "modelo": "Civic", "anio": 2023},
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)
        automovil.refresh_from_db()
        self.assertEqual(automovil.marca, "Honda")

    def test_delete_removes_automovil(self):
        automovil = Automovil.objects.create(marca="Toyota", modelo="Corolla", anio=2022)

        response = self.client.delete(f"/automoviles/{automovil.pk}/")

        self.assertEqual(response.status_code, 204)
        self.assertFalse(Automovil.objects.exists())


class ClienteEndpointTests(TestCase):
    def test_get_lists_seeded_clientes(self):
        response = self.client.get("/clientes/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 4)
        self.assertEqual(response.json()[0]["nombre"], "Ana Perez")

    def test_browsable_api_offers_cliente_form(self):
        response = self.client.get("/clientes/", HTTP_ACCEPT="text/html")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "POST")
        for field in ("nombre", "correo", "telefono"):
            self.assertContains(response, field)

    def test_browsable_api_offers_cliente_update_and_delete(self):
        cliente = Cliente.objects.get(nombre="Ana Perez")

        response = self.client.get(
            f"/clientes/{cliente.pk}/",
            HTTP_ACCEPT="text/html",
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "PUT")
        self.assertContains(response, "DELETE")

    def test_post_creates_cliente(self):
        response = self.client.post(
            "/clientes/",
            {
                "nombre": "Sofia Diaz",
                "correo": "sofia.diaz@example.com",
                "telefono": "+56955555555",
            },
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 201)
        self.assertTrue(Cliente.objects.filter(nombre="Sofia Diaz").exists())

    def test_browsable_api_creates_cliente_from_form_data(self):
        response = self.client.post(
            "/clientes/",
            {
                "nombre": "Sofia Diaz",
                "correo": "sofia.diaz@example.com",
                "telefono": "+56955555555",
            },
            HTTP_ACCEPT="text/html",
        )

        self.assertEqual(response.status_code, 201)
        self.assertTrue(Cliente.objects.filter(nombre="Sofia Diaz").exists())

    def test_put_updates_cliente(self):
        cliente = Cliente.objects.get(nombre="Ana Perez")

        response = self.client.put(
            f"/clientes/{cliente.pk}/",
            {
                "nombre": "Ana Perez",
                "correo": "ana.actualizada@example.com",
                "telefono": "+56911111112",
            },
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)
        cliente.refresh_from_db()
        self.assertEqual(cliente.correo, "ana.actualizada@example.com")

    def test_delete_removes_cliente(self):
        cliente = Cliente.objects.get(nombre="Ana Perez")

        response = self.client.delete(f"/clientes/{cliente.pk}/")

        self.assertEqual(response.status_code, 204)
        self.assertFalse(Cliente.objects.filter(pk=cliente.pk).exists())
