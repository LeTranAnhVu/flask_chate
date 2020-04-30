from main import db, bcrypt, Friend
from main.models import BaseModel
from sqlalchemy import or_

from hashlib import md5


class Group(BaseModel):
    __tablename__ = 'groups'
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('users.id'))
    owned_id = db.Column('owner_id', db.Integer, db.ForeignKey('users.id'))
    display_name = db.Column('display_name', db.String(200), nullable=False)
    public_id = db.Column('public_id', db.String(50), nullable=False, unique=True)
