from main import app
from flask import request
import uuid
from flask_socketio import SocketIO, send, emit, join_room, leave_room

socketio = SocketIO(app, cors_allowed_origins="*")


# @socketio.on('chat')
# def handle_message(msg):
#     print('message:', msg)
#     emit('chat', msg, broadcast=True)

@socketio.on('chat', namespace='/chat_room')
def handle_message2(msg_package):
    print('message:', msg_package)
    print('-------SID------', request.args)
    user_id = msg_package.get('user_id', None)
    room = msg_package.get('room', None)
    message = msg_package.get('message', None)
    fake_id = str(uuid.uuid4())
    if not user_id or not room:
        emit('chat', {'message': 'error'}, room=msg_package['room'], namespace='/chat_room')
    else:
        emit('chat', {'message_id': fake_id, 'message': message, 'user_id': user_id, 'room': room},
             room=msg_package['room'],
             namespace='/chat_room')


@socketio.on('join_room', namespace='/chat_room')
def on_join(data):
    user_id = data['user_id']
    room = data['room']
    join_room(room)
    emit('meta', {'user_id': user_id, 'room': room}, room=room)


@socketio.on('leave_room', namespace='/chat_room')
def on_leave(data):
    user_id = data['user_id']
    room = data['room']
    leave_room(room)
    emit('meta', user_id + ' has left the room.' + room, room=room)
