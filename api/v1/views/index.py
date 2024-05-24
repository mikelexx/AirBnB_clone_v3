#!/usr/bin/python3
"""
defines status route for api
"""
from flask import jsonify
from . import app_views
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.user import User
from models.state import State
from models import storage


@app_views.route('/status', methods=['GET'])
@app_views.route('/status/', methods=['GET'])
def api_status():
    """returns the status of API"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'])
@app_views.route('/stats/', methods=['GET'])
def models_stats():
    """ returns the status of objects"""
    models = {
        "amenities": Amenity,
        "cities": City,
        "places": Place,
        "reviews": Review,
        "states": State,
        "users": User
    }
    stats_dict = {}
    for model in models:
        stats_dict[model] = storage.count(models[model])
    return jsonify(stats_dict)
