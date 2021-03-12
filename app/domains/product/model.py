import uuid

from sqlalchemy.orm import validates

from app.exceptions import BadRequestException
from database import db

_LEN_MAX_FIELD_NAME = 100
_LEN_MAX_FIELD_DESCRIPTION = 100
_LEN_MAX_FIELD_VALUE = 30

category_product = db.Table('category_product',
                            db.Column('product_id', db.String(36), db.ForeignKey('product.id')),
                            db.Column('category_id', db.String(36), db.ForeignKey('category.id')))


class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.String(36), default=str(uuid.uuid4()), primary_key=True, nullable=False, autoincrement=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    value = db.Column(db.Float(), nullable=False)
    fk_category = db.relationship('Category', secondary=category_product, back_populates='fk_product', lazy='joined')

    @validates('name')
    def name_validate(self, key, name: str):
        if not name or len(name) > _LEN_MAX_FIELD_NAME:
            raise BadRequestException(msg=f"Name field cannot be empty or exceed "
                                          f"{_LEN_MAX_FIELD_NAME} limit of characters.")
        return name

    @validates('description')
    def description_validate(self, key, description: str):
        if not description or len(description) > _LEN_MAX_FIELD_DESCRIPTION:
            raise BadRequestException(msg=f"Description field cannot be empty or exceed "
                                          f"{_LEN_MAX_FIELD_DESCRIPTION} limit of characters.")
        return description

    @validates('value')
    def value_validate(self, key, value: str):
        if not value or len(value) > _LEN_MAX_FIELD_VALUE:
            raise BadRequestException(msg=f"Value field cannot be empty or exceed "
                                          f"{_LEN_MAX_FIELD_VALUE} limit of characters.")
        try:
            float(value)
            return value
        except ValueError:
            raise BadRequestException("The field value, must be represented by a float number.")
