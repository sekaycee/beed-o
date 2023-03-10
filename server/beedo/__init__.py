import os

from flask import Flask
from flask_mongoengine import MongoEngine


def create_app(test_config=None):
    '''Create and configure beedo package
    '''
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    # don't forget to replace it with redis or mongodb
    # app.config.from_mapping(
    #     SECRET_KEY='dev',
    #     DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    # )
    app.config['MONGODB_SETTINGS'] = {
        "db": "beedo",
    }
    db = MongoEngine(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return ('Hello, World!')

    return (app)