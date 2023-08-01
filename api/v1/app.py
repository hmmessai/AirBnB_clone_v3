#!/usr/bin/python3
"""API app construction

Creates a flask instance app and starts
when it is called
"""
from api.v1.views import app_views
from flask import Flask, jsonify
from models import storage
import os

app = Flask(__name__)
app.register_blueprint(app_views)

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": 404})

@app.teardown_appcontext
def teardown(exc):
    """Teardown app"""
    storage.close()


if __name__ == '__main__':
    """Starts app when called up on"""
    hostvar = '0.0.0.0'
    portvar = '5000'
    if os.getenv('HBNB_API_HOST'):
        hostvar = os.getenv('HBNB_API_HOST')
    if os.getenv('HBNB_API_PORT'):
        portvar = os.getenv('HBNB_API_PORT')

    app.run(host=hostvar, port=portvar, threaded=True)
