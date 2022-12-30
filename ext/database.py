from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app):
    """app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pymssql://sa:@BRUNO-PC\SQLEXPRESS/ATELIE_DB'"""
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://sa:NXXq2BBdSpUtSFit4VzRF10XLpCN0jsm@dpg-cenghg82i3molpkn2dig-a.oregon-postgres.render.com/ateliedb'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
