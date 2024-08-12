from splitwise.services.users import (
    add_new_user,
    get_all_users,
    get_user,
    update_user_by_id,
    delete_user_by_id,
)
from splitwise.common.utils import is_valid_uuid


def get_users():
    users = get_all_users()
    return users


def add_users(**kwargs):
    payload = kwargs.get("body", {})
    user = add_new_user(payload)
    return user, 201


def get_user_by_id(**kwargs):
    user_id = kwargs.get("userId", "").strip()
    is_valid_uuid(user_id)
    user = get_user(user_id)
    return user


def update_user(**kwargs):
    user_id = kwargs.get("userId", "").strip()
    is_valid_uuid(user_id)
    payload = kwargs.get("body", {})
    user = update_user_by_id(user_id, payload)
    return user


def delete_user(**kwargs):
    user_id = kwargs.get("userId", "").strip()
    is_valid_uuid(user_id)
    delete_user_by_id(user_id)
    return "User deleted", 200
