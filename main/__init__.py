from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_cors import CORS
import jwt

app = Flask(__name__)
db = SQLAlchemy(app)

CORS(app)

bcrypt = Bcrypt(app)

from main.config.env import Env

app.config.from_object(Env)

# engine = create_engine(Env.SQLALCHEMY_DATABASE_URI, convert_unicode=True)

migrate = Migrate(app, db)

from main.models.Friend import Friend
from main.models.User import User
from main.models.Group import Group
from main.models.Conversation import Conversation
from main.models.Message import Message

import main.routes
