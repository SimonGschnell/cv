from flask import Flask
from backend.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__, static_folder="../../dist/static", template_folder="../../dist")



app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app,db)
from . import routes, models,forms


