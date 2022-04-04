from unittest import TestCase

from server.db.db import get_db, SessionLocal


class Test(TestCase):
    def test_get_db(self):
        db = get_db()
        self.assertIsNot(db, get_db())
        self.assertNotEqual(db, get_db())
