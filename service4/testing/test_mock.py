from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestApp(TestBase):


    def test_scene_one(self):
        response = self.client.post(
        url_for("scene"),
        data='Fortune found in a mysterious cavern'
        )
        self.assertIn(b"found", response.data)

    def test_scene_two(self):
        response = self.client.post(
        url_for("scene"),
        data='Fortune found in an intimidating room'
        )
        self.assertIn(b"test2", response.data)

    def test_scene_three(self):
        response = self.client.post(
        url_for("scene"),
        data='Fortune found in a dreamlike headspace'
        )
        self.assertIn(b"pass", response.data)

    def test_scene_four(self):
        response = self.client.post(
        url_for("scene"),
        data='Fears faced in a mysterious cavern'
        )
        self.assertIn(b"spiders.", response.data)

    def test_scene_five(self):
        response = self.client.post(
        url_for("scene"),
        data='Fears faced in an intimidating room'
        )
        self.assertIn(b"leaving", response.data)

    def test_scene_six(self):
        response = self.client.post(
        url_for("scene"),
        data='Fears faced in a dreamlike headspace'
        )
        self.assertIn(b"pass", response.data)

    def test_scene_seven(self):
        response = self.client.post(
        url_for("scene"),
        data='Chance encounter in a mysterious cavern'
        )
        self.assertIn(b"salt", response.data)


    def test_scene_eight(self):
        response = self.client.post(
        url_for("scene"),
        data='Chance encounter in an intimidating room'
        )
        self.assertIn(b"exculpated", response.data)


    def test_scene_nine(self):
        response = self.client.post(
        url_for("scene"),
        data='Chance encounter in a dreamlike headspace'
        )
        self.assertIn(b"luckiest", response.data)