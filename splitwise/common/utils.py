import uuid
from splitwise.common.exceptions import BadRequestError


def is_valid_uuid(id: str):
    try:
        uuid_obj = uuid.UUID(id, version=4)
        return str(uuid_obj) == id
    except ValueError:
        raise BadRequestError("id should be of type: UUID")
