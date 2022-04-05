from unittest import TestCase

from server.security.password import verify_password, get_password_hash


class Test(TestCase):
    password: str = "password"

    def test_verify_password(self):
        self.assertTrue(verify_password(self.password, get_password_hash(self.password)))
        self.assertFalse(verify_password(self.password + "Nope", get_password_hash(self.password)))

    def test_get_password_hash(self):
        self.assertNotEqual(get_password_hash(self.password), get_password_hash(self.password))
