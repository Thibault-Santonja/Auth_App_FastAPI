from unittest import TestCase
from datetime import timedelta

from server.security.token import create_access_token


class Test(TestCase):
    def test_create_access_token(self):
        self.assertIsNotNone(create_access_token({"data": "dict"}, expires_delta=timedelta(minutes=1)))
        self.assertIsNotNone(create_access_token({"data": "dict"}))
