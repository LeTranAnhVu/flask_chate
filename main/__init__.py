from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
db = SQLAlchemy(app)
CORS(app)

from main.config.env import Env
app.config.from_object(Env)

import main.routes
