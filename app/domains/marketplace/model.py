import uuid

from sqlalchemy.orm import validates

from app.exceptions import BadRequestException
from database import db

_LEN_MAX_FIELD_NAME = 100
_LEN_MAX_FIELD_DESCRIPTION = 100
_LEN_MAX_FIELD_VALUE = 30
_LEN_MAX_FIELD_SITE = 100
_LEN_MAX_FIELD_EMAIL = 100
_LEN_MAX_FIELD_PHONE = 16
_LEN_MAX_FIELD_CONTACT_NAME = 100


class Marketplace(db.Model):
    __tablename__ = 'marketplace'

    id = db.Column(db.String(36), default=str(uuid.uuid4()), primary_key=True, nullable=False, autoincrement=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    site = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(16), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    contact_name = db.Column(db.String(100), nullable=False)

    @validates('name')
    def name_validate(self, key, name: str):
        if not name or len(name) > _LEN_MAX_FIELD_NAME:
            raise BadRequestException(msg=f"Name field cannot be empty or exceed "
                                          f"{_LEN_MAX_FIELD_NAME} limit of characters")
        return name

    @validates('description')
    def description_validate(self, key, description: str):
        if not description or len(description) > _LEN_MAX_FIELD_DESCRIPTION:
            raise BadRequestException(msg=f"Description field cannot be empty or exceed "
                                          f"{_LEN_MAX_FIELD_DESCRIPTION} limit of characters")
        return description

    @validates('site')
    def site_validate(self, key, site: str):
        if not site or len(site) > _LEN_MAX_FIELD_SITE:
            raise BadRequestException(msg=f"Site field cannot be empty or exceed "
                                          f"{_LEN_MAX_FIELD_SITE} limit of characters")
        return site

    @validates('email')
    def email_validate(self, key, email: str):
        if not email or len(email) > _LEN_MAX_FIELD_EMAIL:
            raise BadRequestException(msg=f"Email field cannot be empty or exceed "
                                          f"{_LEN_MAX_FIELD_EMAIL} limit of characters")
        return email

    @validates('contact_name')
    def contact_name_validate(self, key, contact_name: str):
        if not contact_name or len(contact_name) > _LEN_MAX_FIELD_CONTACT_NAME:
            raise BadRequestException(msg=f"Contact field cannot be empty or exceed "
                                              f"{_LEN_MAX_FIELD_CONTACT_NAME} limit of characters")
        return contact_name

    @validates('phone')
    def phone_validate(self, key, phone: str):
        if not phone or len(phone) > _LEN_MAX_FIELD_PHONE or not phone.isnumeric():
            raise BadRequestException(msg=f"Phone field cannot be empty or exceed "
                                              f"{_LEN_MAX_FIELD_PHONE} limit of characters")
        return phone
