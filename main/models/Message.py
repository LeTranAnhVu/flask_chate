from main import db, bcrypt, Friend
from main.models import BaseModel
from sqlalchemy import or_

from hashlib import md5


class Message(BaseModel):
    __tablename__ = 'messages'
    owner_id = db.Column('owner_id', db.String(50), db.ForeignKey('users.public_id'))
    conversation_id = db.Column('conversation_id', db.String(50), db.ForeignKey('conversations.public_id'))

    content = db.Column('content', db.String(2000), nullable=False)
    conversation = db.relationship('Conversation', backref=db.backref('messages', lazy='dynamic'), lazy=True)

    def __init__(self, owner_id, conversation_id, content, **kwargs):
        super().__init__(unique_str=None)
        self.owner_id = owner_id
        self.conversation_id = conversation_id
        self.content = content

    public_keys = ['']
