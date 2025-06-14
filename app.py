from flask import Flask
from flask_cors import CORS
from db import db
from routes.auth_routes import auth_bp
from routes.cita_routes import cita_bp

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clinica.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(auth_bp)
app.register_blueprint(cita_bp)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
