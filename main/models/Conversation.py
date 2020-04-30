from main import db, bcrypt, Friend
from main.models import BaseModel
from sqlalchemy import or_

from hashlib import md5


class Conversation(BaseModel):
    __tablename__ = 'conversations'
    user1_id = db.Column('user1_id', db.Integer, db.ForeignKey('users.id'))
    user2_id = db.Column('user2_id', db.Integer, db.ForeignKey('users.id'))
    group_id = db.Column('group_id', db.Integer, db.ForeignKey('users.id'))
    public_id = db.Column('public_id', db.String(50), nullable=False, unique=True)
