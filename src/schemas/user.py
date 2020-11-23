import marshmallow

from . import ma
from models import User


class UserSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = User
        fields = ("email", "full_name", "avatar_url", "created_at")


class UserFullSchema(ma.SQLAlchemyAutoSchema):
    created_at = ma.auto_field()

    class Meta:
        model = User
        fields = ("email", "full_name", "password", "avatar_url", "created_at")


class UserQueryArgsSchema(marshmallow.Schema):
    email = marshmallow.fields.String()


class UserSlimSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = User
        fields = ("full_name", "avatar_url", "is_active")
