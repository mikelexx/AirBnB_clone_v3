#!/usr/bin/python3
"""
defines status route for api
"""
from flask import jsonify, abort, request, make_response
from . import app_views
from models.state import State
from models import storage


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_states_objs():
    """
    Retrieves the list of all Stae Objects
    """
    states = storage.all("State")
    states_list = []
    for key, state in states.items():
        states_list.append(state.to_dict())
    return jsonify(states_list)


@app_views.route('/states/<state_id>', methods=['GET'])
def get_state_obj(state_id):
    """
    Retrieves a State object
    """
    state = storage.get("State", state_id)
    if not state:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route('/states/<state_id>',
                 methods=['DELETE'],
                 strict_slashes=False)
def delete_state_obj(state_id):
    """
    Deletes a State object
    """
    state = storage.get("State", state_id)
    if not state:
        abort(404)
    storage.delete(state)
    storage.save()
    return jsonify({}), 200


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state_obj():
    """
    Creates a State object
    """
    data = request.get_json()
    if not data:
        abort(400, "Not a JSON")
    if "name" not in data:
        abort(400, "Missing name")
    state = State(**data)
    storage.new(state)
    storage.save()
    return jsonify(state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'])
def update_state_obj(state_id):
    """
    Updates a State object
    """
    data = request.get_json()
    if not data:
        abort(400, "Not a JSON")
    state = storage.get("State", state_id)
    if not state:
        abort(404)
    for key, val in data.items():
        if hasattr(state, key) and key != 'create_at'\
                   and key != 'updated_at' and key != 'id':
            setattr(state, key, val)
    storage.save()
    return jsonify(state.to_dict()), 200
