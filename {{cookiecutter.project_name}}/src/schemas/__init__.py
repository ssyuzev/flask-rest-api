# flake8: noqa
from flask_marshmallow import Marshmallow
ma = Marshmallow()

from .healthcheck import HealthcheckSchema
from .user import UserSchema, UserQueryArgsSchema, UserFullSchema, UserSlimSchema


__all__ = ["UserSchema", "UserQueryArgsSchema", "UserFullSchema", "UserSlimSchema", "HealthcheckSchema"]
