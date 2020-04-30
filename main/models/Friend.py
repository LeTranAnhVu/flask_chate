from main import db
from main.models import BaseModel
from sqlalchemy import or_, and_


class Friend(BaseModel):
    __tablename__ = 'friends'
    user1_id = db.Column('user1_id', db.Integer, db.ForeignKey('users.id'))
    user2_id = db.Column('user2_id', db.Integer, db.ForeignKey('users.id'))

    @staticmethod
    def is_existed(user1_id, user2_id):
        # check if not exits
        friend_row = Friend.query.filter(and_(or_(Friend.user1_id == user1_id, Friend.user1_id == user2_id),
                                              or_(Friend.user2_id == user1_id, Friend.user2_id == user2_id))).first()

        return False if friend_row is None else True
