from unittest import TestCase

from server.settings.fast_api import Settings, APP_NAME, CONTACT_MAIL


class TestSettings(TestCase):
    def test_setting(self):
        setting = Settings()
        self.assertEqual(setting.app_name, APP_NAME)
        self.assertEqual(setting.admin_email, CONTACT_MAIL)
