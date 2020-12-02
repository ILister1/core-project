from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestApp(TestBase):

    def test_theme(self):
        themes = [b"Fortune found in", b"Fears faced in", b"Chance encounter in"]
        response = self.client.get(url_for('theme'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(response.data, themes)