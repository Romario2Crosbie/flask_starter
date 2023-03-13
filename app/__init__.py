from flask import Flask
from .config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config.from_object(Config)
app.config['SECRET_KEY'] = "6549d4e1c88526a1e0d99df2c370d0981f580fb8b873e3eb4b62b0b70cafa325"  # Ideally you'd want this to be a much longer and more random string
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://romario:Ricardo1421@localhost/project1'
app.config['UPLOAD_FOLDER'] = './uploads'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed

db = SQLAlchemy(app)
# Instantiate Flask-Migrate library here
migrate = Migrate(app, db)


from app import views