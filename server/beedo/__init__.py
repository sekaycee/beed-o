import os

from flask import Flask, render_template
from flask.json import JSONEncoder
from flask_cors import CORS

from bson import json_util, ObjectId
from datetime import datetime, timedelta

# from beedo.api.tasks import tasks_api_v1

class MongoJsonEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return (obj.strftime("%Y-%m-%d %H:%M:%S"))
        if isinstance(obj, ObjectId):
            return (str(obj))
        return (json_util.default(obj, json_util.CANONICAL_JSON_OPTIONS))


def create_app():
    ''' Create and configure beedo package '''

    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    STATIC_FOLDER = os.path.join(APP_DIR, 'build/static')
    TEMPLATE_FOLDER = os.path.join(APP_DIR, 'build')

    app = Flask(__name__, static_folder=STATIC_FOLDER,
                template_folder=TEMPLATE_FOLDER,
                )
    CORS(app)
    app.json_encoder = MongoJsonEncoder
    # app.register_blueprint(tasks_api_v1)

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def serve(path):
        return (render_template('index.html'))

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return ('Hello, World!')

    return (app)
