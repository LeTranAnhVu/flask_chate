from main import db, bcrypt, Friend
from main.models import BaseModel
from sqlalchemy import or_

from hashlib import md5


class Message(BaseModel):
    __tablename__ = 'messages'
    owner_id = db.Column('owner_id', db.Integer, db.ForeignKey('users.id'))
    conversation_id = db.Column('conversation_id', db.Integer, db.ForeignKey('conversations.id'))
    public_id = db.Column('public_id', db.String(50), nullable=False, unique=True)
    content = db.Column('content', db.String(2000), nullable=False)
    conversation = db.relationship('Conversation', backref=db.backref('messages', lazy='dynamic'), lazy=True)
