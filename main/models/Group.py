from main import db, bcrypt, Friend
from main.models import BaseModel
from sqlalchemy import or_

from hashlib import md5


class Group(BaseModel):
    __tablename__ = 'groups'
    user_id = db.Column('user_id', db.String(50), db.ForeignKey('users.public_id'))
    owned_id = db.Column('owner_id', db.String(50), db.ForeignKey('users.public_id'))
    display_name = db.Column('display_name', db.String(200), nullable=False)
