from unittest import TestCase
from fastapi.testclient import TestClient

from server.settings.variables import API_ROOT
from server.settings.fast_api import app, settings
from server.api import routes


class Test(TestCase):
    client: TestClient

    def setUp(self) -> None:
        app.include_router(routes.router, prefix=API_ROOT, tags=["default"])
        self.client = TestClient(app)

    def test_home(self):
        response = self.client.get(API_ROOT + "/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result": "Hello !"})

    def test_info(self):
        response = self.client.get(API_ROOT + "/info")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "app_name": settings.app_name,
            "admin_email": settings.admin_email
        })
