from main import db
from datetime import datetime
import random
from hashlib import md5
from main.helpers.common import without_items


class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column('id', db.Integer, autoincrement=True, primary_key=True)
    public_id = db.Column('public_id', db.String(50), primary_key=True, nullable=False, unique=True)
    created_at = db.Column('created_at', db.DateTime, default=datetime.utcnow())
    updated_at = db.Column('updated_at', db.DateTime, onupdate=datetime.utcnow())

    public_keys = []

    def __init__(self, unique_str=None):
        self.public_id = self.gen_public_id(unique_str)

    @staticmethod
    def gen_public_id(unique_str=None):
        if unique_str:
            return md5(unique_str.encode('utf8')).hexdigest()
        else:
            pre = str(datetime.utcnow().timestamp() * 1000000)
            post = str(random.randint(1, 1000000))
            rd = pre + post
            return md5(rd.encode('utf8')).hexdigest()

    def to_json(self, except_keys=None, parent_models=None, extra_keys=None):
        d = dict()

        # re-asign
        except_keys = [] if except_keys is None else except_keys
        parent_models = set() if parent_models is None else parent_models
        extra_keys = [] if extra_keys is None else extra_keys
        parent_models.add(self.__class__)
        keys = list({*extra_keys, *self.public_keys})
        for key in without_items(keys, except_keys):
            data = getattr(self, key, None)
            if isinstance(data, db.Model) and data.__class__ not in parent_models:
                d[key] = data.to_json(parent_models=parent_models)
            elif isinstance(data, list) and len(data) > 0 and isinstance(data[0], db.Model):
                d[key] = [in_model.to_json(parent_models=parent_models.copy()) for in_model in data]
            elif not isinstance(data, db.Model):
                d[key] = data
            else:
                pass
        return d
