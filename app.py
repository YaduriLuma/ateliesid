from flask import Flask
from ext import database, configuration
import views

app = Flask(__name__)

configuration.init_app(app)
db = database.init_app(app)
app.register_blueprint(views.bp)

if __name__ == "__main__":
    app.run(debug=True)
