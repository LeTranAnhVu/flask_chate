from main import app
from main.config.env import Env
from main.socket import socketio

if __name__ == '__main__':
    app.run(host=Env.HOST_IP, port=Env.PORT)
    socketio.run(app)
