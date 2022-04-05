from unittest import TestCase

from server.schemas.Token import Token, TokenData


class Test(TestCase):
    def test_token(self):
        token = Token()
        self.assertIsNone(token.token_type)
        self.assertIsNone(token.access_token)

    def test_token_data(self):
        token_data = TokenData()
        self.assertIsNone(token_data.user_id)
        self.assertIsNone(token_data.user_name)
        self.assertIsNone(token_data.is_admin)
        self.assertIsNone(token_data.exp)
