from splitwise.data_access.users import (
    add_user_to_db,
    get_users_from_db,
    get_user_from_db,
    update_user_in_db,
    delete_user_from_db,
)
from splitwise.common.exceptions import NotFoundError


def add_new_user(payload: dict):
    name = payload.get("name")
    email = payload.get("email")
    phone = payload.get("phone")

    user = add_user_to_db(name, email, phone)
    return user.as_dict()


def get_all_users():
    users = get_users_from_db()
    users = [user.as_dict() for user in users]
    return {"users": users}


def get_user(user_id):
    user = get_user_from_db(user_id)
    return user.as_dict()


def update_user_by_id(user_id, payload):
    user = update_user_in_db(user_id, payload)
    return user.as_dict()


def delete_user_by_id(user_id):
    delete_user_from_db(user_id)
