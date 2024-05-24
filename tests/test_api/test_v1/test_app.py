from api.v1.app import app
import flask
import json
import unittest

class FlaskAppTestCase(unittest.TestCase):
    """ test our application """
    def setUp(self):
        """ prepare the app for testing """
        self.app = app.test_client()
        self.app.testing = True

    def test_resource_not_found(self):
        """ test query for nonexistent route returns 404 error"""
        response = self.app.get('/api/v1/nop')
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.data)
        self.assertEqual(data['error'], 'Not found')

if __name__ == '__main__':
    unittest.main()
