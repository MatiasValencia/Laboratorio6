from django.test import TestCase


class ApiRootTests(TestCase):
    def test_api_root_lists_automobile_endpoints(self):
        response = self.client.get("/", HTTP_ACCEPT="text/html")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Listar Automóviles")
        self.assertContains(response, "Crear Automóviles")
        self.assertContains(response, "/automoviles/")
        self.assertContains(response, "/automoviles/crear/")
