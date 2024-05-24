#!/usr/bin/python3
"""
tests the state api
"""
import json
import flask
import unittest
from api.v1.app import app
from flask import Flask


class StateTestCase(unittest.TestCase):
    """ test our application """

    def setUp(self):
        """ prepare the app for testing """
        self.app = app.test_client()
        self.app.testing = True

    def test_get_states_objs(self):
        """ tests the function returns list of State Objects"""
        response = self.app.get('/api/v1/states')
        data = json.loads(response.data.decode('utf-8'))
        attributes = ["created_at", "updated_at", "id"]
        for obj in data:
            assert obj["__class__"] == "State"
            for attr in attributes:
                assert attr in obj
                assert type(obj[attr]) is str

    def test_get_state_obj(self):
        """ tests the function Retrieves State Object"""
        response = self.app.get('/api/v1/states/22')
        assert json.loads(
            response.data.decode('utf-8'))['error'] == "Not found"
        assert response.status_code == 404
        response = self.app.get('/api/v1/states')
        states_data = json.loads(response.data.decode('utf-8'))
        for state in states_data:
            state_id = state["id"]
            response = self.app.get('/api/v1/states/{}'.format(state_id))
            data = json.loads(response.data.decode('utf-8'))
            attributes = ["created_at", "updated_at", "id"]
            for attr in attributes:
                assert attr in data
                assert type(data[attr]) is str
            assert data["id"] == state_id
            break

    def test_delete_state_obj(self):
        response = self.app.get('/api/v1/states/22')
        assert json.loads(
            response.data.decode('utf-8'))['error'] == "Not found"
        assert response.status_code == 404
        response = self.app.get('/api/v1/states')
        states_data = json.loads(response.data.decode('utf-8'))
        for state in states_data:
            state_id = state["id"]
            response = self.app.delete('/api/v1/states/{}'.format(state_id))
            data = json.loads(response.data.decode('utf-8'))
            assert len(data) == 0
            assert response.status_code == 200

    def test_create_state_obj(self):
        """Tests creation of State object via api"""
        data = {"name": "test_name"}
        response = self.app.get('/api/v1/states')
        old_data = json.loads(response.data.decode('utf-8'))
        response = self.app.post('/api/v1/states', json=data)
        data = json.loads(response.data.decode('utf-8'))
        assert response.status_code == 201
        assert data["name"] == "test_name"
        response = self.app.get('/api/v1/states', data=data)
        updated_data = json.loads(response.data.decode('utf-8'))
        assert (len(updated_data) - len(old_data)) == 1

    def test_update_state_obj(self):
        """Tests that chosen state objects get updated properly"""
        response = self.app.get('/api/v1/states')
        data = json.loads(response.data.decode('utf-8'))
        for state in data:
            data = {"name": "USA"}
            state_id = state["id"]
            response = self.app.get('/api/v1/states')
            old_states = json.loads(response.data.decode('utf-8'))
            response = self.app.put('/api/v1/states/{}'.format(state_id),
                                    json=data)
            assert response.status_code == 200
            assert data["name"] == "USA"
            response = self.app.get('/api/v1/states/{}'.format(state_id),
                                    data=data)
            updated_state = json.loads(response.data.decode('utf-8'))
            assert updated_state["name"] == "USA"
            response = self.app.get('/api/v1/states')
            new_states = json.loads(response.data.decode('utf-8'))
            assert len(new_states) == len(old_states)
            break


if __name__ == '__main__':
    unittest.main()
