from flask import Flask
from atelie.ext import configuration, database, views

app = Flask(__name__)

configuration.init_app(app)
database.init_app(app)
views.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)
