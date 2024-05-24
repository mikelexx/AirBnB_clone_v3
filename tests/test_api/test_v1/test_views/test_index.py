#!/usr/bin/python3
""" this module tests the default api endpoint"""
import json
import flask
import unittest
from api.v1.app import app
from flask import Flask


class DefaultTestCase(unittest.TestCase):
    """ tests the status of api"""

    def setUp(self):
        """ prepare the app for testing """
        self.app = app.test_client()
        self.app.testing = True

    def test_api_status(self):
        """ tests the status api"""
        response = self.app.get('/api/v1/status')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        assert data["status"] == "OK"

    def test_models_stats(self):
        """ tests the status of all models"""
        response = self.app.get('/api/v1/stats')
        data = json.loads(response.data.decode('utf-8'))
        for model in [
                "amenities", "cities", "places", "reviews", "states", "users"
        ]:
            if model in data:
                self.assertIs(type(data[model]), int)


if __name__ == '__main__':
    unittest.main()
