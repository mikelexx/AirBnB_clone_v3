#!/usr/bin/python3
"""
tests the user api
"""
import json
import flask
import unittest
from api.v1.app import app
from flask import Flask
from models.user import User
from models import storage


class UserTestCase(unittest.TestCase):
    """ test our application """

    def test_get_users(self):
        """ tests api endpoint for all User resorces """
        with app.test_client() as c:
            response = c.get('/api/v1/users')
            self.assertEqual(response.status_code, 200)
            response = c.get('/api/v1/users/')
            self.assertEqual(response.status_code, 200)

    def test_get_user(self):
        """ tests api for getting  specific user works """
        with app.test_client() as c:
            user = User(first_name="Michael",
                        last_name="Murithi",
                        email="123@abc.com",
                        password="mikelexx")
            storage.new(user)
            response = c.get('api/v1/users/{}'.format(user.id))
            self.assertEqual(response.status_code, 200)

    def test_create_user(self):
        """ test function creates a user properly """
        with app.test_client() as c:
            response = c.post('/api/v1/users/',
                              data=json.dumps(
                                  dict(email="murithimichael254@gmail.com",
                                       password="mikelexx")),
                              content_type="application/json")
            self.assertEqual(response.status_code, 201)

    def test_update_user(self):
        """ tests api for updating a user works """
        with app.test_client() as c:
            user = User(first_name="Michael",
                        last_name="Murithi",
                        email="murithimichael254@gmail.com",
                        password="mikelexx")
            storage.new(user)
            storage.save()
            response = c.put('api/v1/users/{}'.format(user.id),
                             data=json.dumps({
                                 "first_name": "Nancie",
                                 "last_name": "Nkatha"
                             }),
                             content_type="application/json")
            self.assertEqual(response.status_code, 200)

    def test_delete_user(self):
        """ test api for deleting users works properly """
        with app.test_client() as c:
            user = User(first_name="Michael",
                        last_name="Murithi",
                        email="murithimichael254@gmail.com",
                        password="mikelexx")
            storage.new(user)
            storage.save()
            response = c.get('api/v1/users/{}'.format(user.id))
            self.assertEqual(response.status_code, 200)
            response = c.delete('api/v1/users/{}'.format(user.id))
            self.assertEqual(response.status_code, 200)
            response = c.get('api/v1/users/{}'.format(user.id))
            self.assertEqual(response.status_code, 404)

    if __name__ == '__main__':
        unittest.main()
