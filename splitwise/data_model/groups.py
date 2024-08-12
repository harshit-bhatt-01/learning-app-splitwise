import uuid
from app import db

class Groups(db.Model):
    __tablename__ = "groups"
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String, unique=True, nullable=False)
    users = db.Column(db.JSON, nullable=False)

    def as_dict(self) -> dict:
        return {
            "id" : self.id,
            "name" : self.name,
            "users" : self.users
        }
