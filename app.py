"""
    JSON Database API

    Copyright (c) 2024 Dmytro Ostapenko. All rights reserved.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

import json

from flask import Flask, request, Response
from flask_cors import CORS, cross_origin

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

_GLOBAL_DATABASE_PATH = 'database.json'
_GLOBAL_RESPONSE_MIME_TYPE = 'application/json'


@app.route("/")
@cross_origin()
def index():
    return Response('{"message": "Welcome to the JSON Database API", "code": 200}', status=200, mimetype=_GLOBAL_RESPONSE_MIME_TYPE)


@app.route("/api/v1/read")
@cross_origin()
def hello_world():
    path = request.args.get('path')

    if path:
        return Response(read_child(path), status=200, mimetype=_GLOBAL_RESPONSE_MIME_TYPE)
    else:
        return Response(read_json(), status=200, mimetype=_GLOBAL_RESPONSE_MIME_TYPE)


@app.route("/api/v1/write")
@cross_origin()
def write():
    path = request.args.get('path')
    value = request.args.get('value')
    _type = request.args.get('type')

    if path:
        if value and _type != 'null':
            if _type == 'json':
                value = json.loads(value)

            write_child(path, value, _type)
            return Response(str(read_child(path)), status=200, mimetype=_GLOBAL_RESPONSE_MIME_TYPE)
        elif _type == 'null':
            write_child(path, value, _type)
            return Response('{"message": "Data deleted successfully", "code": 200}', status=200, mimetype=_GLOBAL_RESPONSE_MIME_TYPE)
        else:
            return Response('{"message": "A value must be specified", "code": 400}', status=400, mimetype=_GLOBAL_RESPONSE_MIME_TYPE)
    else:
        if _type == 'clear':
            write_json("{}")
            return Response('{"message": "Database cleared successfully", "code": 200}', status=200, mimetype=_GLOBAL_RESPONSE_MIME_TYPE)
        else:
            return Response('{"message": "A path must be specified", "code": 400}', status=400, mimetype=_GLOBAL_RESPONSE_MIME_TYPE)


@app.route("/api/v1/delete")
@cross_origin()
def delete():
    path = request.args.get('path')

    if path:
        write_child(path, None, 'null')
        return Response('{"message": "Data deleted successfully", "code": 200}', status=200, mimetype=_GLOBAL_RESPONSE_MIME_TYPE)
    else:
        return Response('{"message": "A path must be specified", "code": 400}', status=400, mimetype=_GLOBAL_RESPONSE_MIME_TYPE)


@app.errorhandler(404)
def page_not_found(_):
    return Response('{"message": "The requested URL was not found on the server", "code": 404}', status=404, mimetype=_GLOBAL_RESPONSE_MIME_TYPE)


@app.errorhandler(403)
def forbidden(_):
    return Response('{"message": "You don\'t have the permission to access the requested resource", "code": 403}', status=403, mimetype=_GLOBAL_RESPONSE_MIME_TYPE)


@app.errorhandler(401)
def unauthorized(_):
    return Response('{"message": "You are not authorized to access the requested resource", "code": 401}', status=401, mimetype=_GLOBAL_RESPONSE_MIME_TYPE)


@app.errorhandler(500)
def internal_server_error(_):
    return Response('{"message": "The server encountered an internal error and was unable to complete your request", "code": 500}', status=500, mimetype=_GLOBAL_RESPONSE_MIME_TYPE)


def read_child(path):
    data = read_json()
    data = json.loads(data)
    children = path.split('/')
    for child in children:
        try:
            data = data[child]
        except KeyError:
            return '{"message": "Data not found", "code": 404}'

    return str(data)


def write_child(path, value, datatype='json'):
    data1 = read_json()
    data1 = json.loads(data1)

    children = path.strip('/').split('/')
    current_level = data1

    for i, child in enumerate(children, 1):  # enumerate gives you both index and value starting from 1
        if i == len(children):
            if datatype == 'null':
                current_level.pop(child, None)
            else:
                current_level[child] = value
        else:
            current_level = current_level.setdefault(child, {})  # Use setdefault to handle missing keys

    data1 = json.dumps(data1)
    write_json(data1)


def read_json():
    with open(_GLOBAL_DATABASE_PATH, 'r') as file:
        data = file.read()
    return data


def write_json(data):
    with open(_GLOBAL_DATABASE_PATH, 'w') as file:
        file.write(data)


if __name__ == "__main__":
    app.run()
