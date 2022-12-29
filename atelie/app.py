from flask import Flask
from atelie.ext import configuration, database, views

app = Flask(__name__)

configuration.init_app(app)
database.init_app(app)
views.init_app(app)


def minimal_app(**config):
    app = Flask(__name__)
    configuration.init_app(app)
    return app


def create_app(**config):
    app = minimal_app(**config)
    return app
