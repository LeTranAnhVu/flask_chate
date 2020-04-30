from main import db
from datetime import datetime


from main.helpers.common import without_items


class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column('id', db.Integer, primary_key=True)
    created_at = db.Column('created_at', db.DateTime, default=datetime.utcnow())
    updated_at = db.Column('updated_at', db.DateTime, onupdate=datetime.utcnow())

    public_keys = []

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

