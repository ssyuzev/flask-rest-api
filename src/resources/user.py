from flask.views import MethodView
from flask_smorest import Blueprint, abort

from schemas import UserSchema, UserFullSchema, UserSlimSchema
from repositories import UserRepository


user_api = Blueprint(
    'users', 'users', url_prefix='/api/v1/users/',
    description='Operations with users'
)


@user_api.route('/')
class Users(MethodView):

    @user_api.response(UserSchema(many=True))
    def get(self):
        """List users"""
        return UserRepository.all()

    @user_api.arguments(UserFullSchema)
    @user_api.response(UserSchema, code=201)
    def post(self, new_data):
        """Add a new user"""
        result, created = UserRepository.create(**new_data)
        if not created:
            abort(409, message="User already exists.")
        return result


@user_api.route('/<email>')
class UserByEmail(MethodView):

    @user_api.response(UserSchema)
    def get(self, email):
        """Get user by email"""
        item = UserRepository.get(email)
        if not item:
            abort(404, message='Item not found.')
        return item

    @user_api.arguments(UserSlimSchema)
    @user_api.response(UserSchema)
    def put(self, update_data, email):
        """Update existing user"""
        item = UserRepository.update(email, update_data)
        if not item:
            abort(404, message='Item not found.')
        return item

    @user_api.response(code=204)
    def delete(self, email):
        """Delete user"""
        deleted = UserRepository.delete(email)
        if not deleted:
            abort(404, message='Item not found.')
        return deleted
