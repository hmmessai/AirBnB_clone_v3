#!/usr/bin/python3
"""Views definition?"""
from api.v1.views.index import *
from flask import Flask, Blueprint

app_views = Blueprint('/api/v1', __name__)
