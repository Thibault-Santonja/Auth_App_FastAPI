from unittest import TestCase

from server.db.model_user import User


class TestUser(TestCase):
    def test_user(self):
        user = User()
        self.assertIsNone(user.username)
        self.assertIsNone(user.password)
        self.assertIsNone(user.email)
        self.assertIsNone(user.id)
        self.assertIsNone(user.created_at)
        self.assertIsNone(user.updated_at)
        self.assertIsNone(user.is_active)
        self.assertIsNone(user.is_admin)
