import datetime

from . import db
from .abc import BaseModel
from .utils import set_password


class User(db.Model, BaseModel):
    email = db.Column(db.String, primary_key=True, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    full_name = db.Column(db.String, nullable=True)
    avatar_url = db.Column(db.String, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True, nullable=False)

    def __init__(
        self,
        email: str,
        password: str,
        full_name: str = "",
        avatar_url: str = "",
    ):
        self.email = email
        self.password = set_password(password)
        self.full_name = full_name
        self.avatar_url = avatar_url

    def __repr__(self):
        return f"<User: {self.email}>"
