from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_scene_on_page(self):
        with patch("requests.get") as g:
            with patch("requests.post") as p:
                g.return_value.text = "Fortune found in"
                p.return_value.text = "a mysterious cavern"

                response = self.client.get(url_for("index"))
                self.assertIn(b"Fortune found in a mysterious cavern", response.data)