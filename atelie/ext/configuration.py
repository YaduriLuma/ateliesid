from dynaconf import FlaskDynaconf
from flask_bootstrap import Bootstrap


def init_app(app):
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    FlaskDynaconf(app)
    Bootstrap(app)
    app.config['TITLE'] = 'Social'
