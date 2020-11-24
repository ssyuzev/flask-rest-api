from sqlalchemy.exc import IntegrityError
from models import User, db


class UserRepository:

    @staticmethod
    def create(email: str, password: str, full_name: str, avatar_url: str) -> dict:
        """ Create user """
        result: dict = {}
        created = True
        try:
            user = User(email=email, password=password, full_name=full_name, avatar_url=avatar_url)
            user.save()
            result = user
        except IntegrityError:
            User.rollback()
            created = False
        return result, created

    @staticmethod
    def get(email: str) -> dict:
        """Query a user by user email."""
        user: dict = {}
        user = User.query.filter_by(email=email).first_or_404()
        return user

    @staticmethod
    def all() -> list:
        users = []
        users = User.query.filter_by(is_active=True)
        return users

    @staticmethod
    def delete(email: str) -> bool:
        user = UserRepository.get(email)
        if not user:
            return False
        db.session.delete(user)
        db.session.commit()
        return True

    @staticmethod
    def update(email: str, update_data: dict) -> bool:
        user = UserRepository.get(email)
        new_avatar_url = update_data.get("avatar_url")
        if new_avatar_url:
            user.avatar_url = new_avatar_url
        new_full_name = update_data.get("full_name")
        if new_full_name:
            user.full_name = new_full_name
        user.is_active = update_data.get("is_active", True)
        user.save()
        return user
