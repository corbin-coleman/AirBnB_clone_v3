#!/usr/bin/python3
"""
index
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage

@app_views.route('/status', strict_slashes=False)
def status_ok():
    return jsonify({'status': "OK"})

@app_views.route('/stats', strict_slashes=False)
def stats():
    objects = {}
    objects['amenities'] = storage.count('Amenity')
    objects['cities'] = storage.count('City')
    objects['places'] = storage.count('Place')
    objects['reviews'] = storage.count('Review')
    objects['states'] = storage.count('State')
    objects['users'] = storage.count('User')
    return jsonify(objects)
