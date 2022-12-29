from flask_sqlalchemy import SQLAlchemy


def init_app(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pymssql://sa:@BRUNO-PC\SQLEXPRESS/ATELIE_DB'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db = SQLAlchemy(app)
