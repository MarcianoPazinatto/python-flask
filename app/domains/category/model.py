import uuid

from sqlalchemy.orm import validates

from app.domains.product.model import category_product
from app.exceptions import BadRequestException
from database import db

_LEN_MAX_FIELD_NAME = 100
_LEN_MAX_FIELD_DESCRIPTION = 100


class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.String(36), default=str(uuid.uuid4()), primary_key=True, nullable=False, autoincrement=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    fk_product = db.relationship('Product', secondary=category_product, back_populates='fk_category', lazy='joined')

    @validates('name')
    def name_validate(self, key, name: str):
        if not name or len(name) > _LEN_MAX_FIELD_NAME:
            raise BadRequestException(msg=f"Name field cannot be empty or exceed "
                                          f"{_LEN_MAX_FIELD_NAME} limit of characters")
        return name

    @validates('description')
    def description_validate(self, key, description: str):
        if not description or len(description) > _LEN_MAX_FIELD_DESCRIPTION:
            raise BadRequestException(msg=f"Name field cannot be empty or exceed "
                                          f"{_LEN_MAX_FIELD_DESCRIPTION} limit of characters")
        return description
