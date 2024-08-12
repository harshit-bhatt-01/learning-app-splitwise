from splitwise.data_model.users import Users
from extensions import db
from splitwise.common.exceptions import NotFoundError


def add_user_to_db(name, email, phone):
    user = Users(name=name, email=email, phone=phone)
    db.session.add(user)
    db.session.commit()
    return user


def get_users_from_db():
    users = Users.query.all()
    return users


def get_user_from_db(user_id):
    user = Users.query.get(user_id)
    if not user:
        raise NotFoundError("User not found")
    return user


def update_user_in_db(user_id, payload):
    user = Users.query.get(user_id)
    if not user:
        raise NotFoundError("User not found")
    if user:
        user.name = payload.get("name", user.name)
        user.email = payload.get("email", user.email)
        user.phone = payload.get("phone", user.phone)

        db.session.commit()
        return user


def delete_user_from_db(user_id):
    user = Users.query.get(user_id)
    if not user:
        raise NotFoundError("User not found")
    db.session.delete(user)
    db.session.commit()
