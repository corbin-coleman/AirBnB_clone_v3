#!/usr/bin/python3
"""
index
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage

@app_views.route('/status')
def status_ok():
    return jsonify({'status': "OK"})

@app_views.route('/api/v1/stats')
def stats():
    objects = {}
    objects['amenities'] = storage.count('Amenity')
    objects['cities'] = storage.count('City')
    objects['places'] = storage.count('Place')
    objects['reviews'] = storage.count('Review')
    objects['states'] = storage.count('State')
    objects['users'] = storage.count('User')

