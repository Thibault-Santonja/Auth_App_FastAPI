from unittest import TestCase

from sqlalchemy.orm import Session

from server.db.db import get_db
from server.crud.user import authenticate_user


class Test(TestCase):
    db: Session = next(get_db()),

    def test_authenticate_user(self):
        self.assertIsNone(authenticate_user(self.db[0], "adminfake", "password"))
        self.assertIsNone(authenticate_user(self.db[0], "admin", "passwordfake"))
        authenticate_user(self.db[0], "admin", "password")
