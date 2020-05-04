from flask import Blueprint, request, abort, g, jsonify
import datetime
from main import db, User, Conversation, Message
import random
from faker import Faker

blueprint = Blueprint('seed', __name__)


@blueprint.route('/conversation')
def conversation():
    users = User.query.limit(3).all()
    if len(users) >= 3:
        con1 = Conversation(user1_id=users[0].public_id, user2_id=users[1].public_id)
        con2 = Conversation(user1_id=users[0].public_id, user2_id=users[2].public_id)
        con3 = Conversation(user1_id=users[2].public_id, user2_id=users[1].public_id)
        db.session.add_all([con1, con2, con3])
        db.session.commit()
    else:
        return 'there is not enough users, minimun is 3', 400

    return 'seed success', 200


@blueprint.route('/message')
def message():
    conversations = Conversation.query.limit(3).all()
    fake = Faker()
    if len(conversations) >= 3:
        for con in conversations:
            turns = random.randint(10, 30)
            user1_id = con.user1_id
            user2_id = con.user2_id
            for turn in range(turns):
                _mes_type = random.randint(0, 1)
                _who_type = random.randint(0, 1)
                _text_rd = random.randint(40, 500)
                sen = fake.sentence() if _mes_type == 1 else fake.text(_text_rd)
                owner_id = user1_id if _who_type == 1 else user2_id
                message = Message(owner_id=owner_id, content=sen, conversation_id=con.public_id)
                db.session.add(message)
        db.session.commit()



    else:
        return 'there is not enough conversation, minimun is 3', 400

    return 'seed success', 200
