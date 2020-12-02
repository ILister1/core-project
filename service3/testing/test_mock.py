from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import random

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestApp(TestBase):

    def test_setting(self):

        settings = [b"a dreamlike headspace", b"a mysterious cavern", b"an intimidating room"]
        setting = random.choices(settings)

        response = self.client.get(url_for('setting'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(response.data, settings)