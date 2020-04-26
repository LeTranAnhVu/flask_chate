from main.config import BaseEnv


class Env(BaseEnv):
    SALT = "secret_key"
    DEBUG = True
    SQLALCHEMY_ECHO = True
    HOST_IP = 'localhost'
    PORT = '8000'
    SERVER_NAME = HOST_IP + ":" + PORT
    DATABASE_USER = 'root'
    DATABASE_PASSWORD = ''
    DATABASE_NAME = 'db_chate'
    DATABASE_HOST = 'localhost'
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DATABASE_USER}{':' + DATABASE_PASSWORD if DATABASE_PASSWORD else ''}@{DATABASE_HOST}/{DATABASE_NAME}"
