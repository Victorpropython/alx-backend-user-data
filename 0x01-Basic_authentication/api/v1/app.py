#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os
from api.v1.views.index import app_views

#  importing the auth class based on Auth_TYPE

auth = None
Auth_TYPE = getenv("AUTH_TYPE")

if AUTH_TYPE == "auth":
    from api.v1.auth.auth import Auth
    auth = Auth()

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.errorhandler(401)
def unauthorized(error) -> str:
    """Unauthorized error handle
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """For forbidden error handler
    """
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def before_request():
    #  skipping the auth if its not set
    if auth is None:
        return

    #  List of endpoints that dot need authorization
    open_paths = ['api/v1/status/', '/api/v1/unauthorizes',
                  'api/v1/forbbiden/']
    #  Checking if request path require authorization
    if not auth.require_auth(request.path, open_paths):
        return

    #  checks for authorization Header
    if auth.authorization_header(request) is None:
        abort(401)

    # Checks if user is authorized
    if auth.current_user(request) is None:
        abort(403)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
