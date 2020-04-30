from main import db, bcrypt, Friend
from main.models import BaseModel
from sqlalchemy import or_

from hashlib import md5


class User(BaseModel):
    __tablename__ = 'users'
    username = db.Column('username', db.String(200), nullable=False, unique=True)
    password = db.Column('password', db.Text, nullable=False)
    display_name = db.Column('display_name', db.String(500), nullable=False)
    public_id = db.Column('public_id', db.String(50), nullable=False, unique=True)
    logined_at = db.Column('logined_at', db.DateTime)

    def __init__(self, display_name, username, password, **kwargs):
        self.username = username
        self.display_name = display_name
        self.password = bcrypt.generate_password_hash(password)
        self.public_id = md5(username.encode('utf8')).hexdigest()

    def verify_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    def friend_list(self):
        own_id = self.id
        friends = Friend.query.filter(or_(Friend.user1_id == own_id, Friend.user2_id == own_id)).all()
        friend_ids = []
        for friend_row in friends:
            friend_id =friend_row.user1_id if friend_row.user1_id != own_id else friend_row.user2_id
            friend_ids.append(friend_id)
        if len(friend_ids) > 0:
            return User.query.filter(User.id.in_(friend_ids)).all()
        else:
            return friend_ids
