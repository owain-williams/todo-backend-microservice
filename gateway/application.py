from flask import Flask, request, Response
from typing import List, Tuple
import requests
import json


def create_application() -> Flask:
    app = Flask(__name__)

    @app.route('api/v1/todo', methods=['POST'])
    def post_todo():
        payload = request.get_json(force=True)
        response = requests.post(
            f'http://localhost:5000/api/v1/todo', data=json.dumps(payload))
        return Response(response.content, response.status_code, response.headers.items())

    

    return app
