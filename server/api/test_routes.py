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

    def test_login_for_access_token_fake_username(self):
        response = self.client.post(API_ROOT + "/auth/login", data={
            'username': 'fakeadmin',
            'password': 'password'
        })
        self.assertEqual(response.status_code, 401)

    def test_login_for_access_token_fake_password(self):
        response = self.client.post(API_ROOT + "/auth/login", data={
            'username': 'admin',
            'password': 'fakepassword'
        })
        self.assertEqual(response.status_code, 401)

    def test_login_for_access_token(self):
        response = self.client.post(API_ROOT + "/auth/login", data={
            'username': 'admin',
            'password': 'password'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.json().keys()), ["access_token", "token_type"])
