import uuid
from database import db


class Marketplace(db.Model):
    __tablename__ = 'marketplace'

    id = db.Column(db.String(36), default=str(uuid.uuid4()), primary_key=True, nullable=False, autoincrement=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    site = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(16), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    contact_name = db.Column(db.String(100), nullable=False)