from main import db, bcrypt, Friend
from main.models import BaseModel
from sqlalchemy import or_

from hashlib import md5


class Conversation(BaseModel):
    __tablename__ = 'conversations'
    user1_id = db.Column('user1_id', db.String(50), db.ForeignKey('users.public_id'))
    user2_id = db.Column('user2_id', db.String(50), db.ForeignKey('users.public_id'))
    group_id = db.Column('group_id', db.String(50), db.ForeignKey('groups.public_id'))

    public_keys = ['user1_id', 'user2_id', 'group_id']

    def __init__(self, user1_id=None, user2_id=None, group_id=None):
        super().__init__(unique_str=None)
        self.user1_id = user1_id
        self.user2_id = user2_id
        self.group_id = group_id
