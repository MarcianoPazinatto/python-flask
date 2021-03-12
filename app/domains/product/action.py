from app.domains.product.model import Product
from database.repository import commit, save
from uuid import uuid4
from typing import List, NoReturn
from app.domains.category.action import get_by_id as get_by_id_category
from app.domains.product.schema import ProductSchema
from app.exceptions import BadRequestException
from re import findall

ProductSchemaMa = ProductSchema()
_LEN_MAX_FIELD_NAME = 100
_LEN_MAX_FIELD_DESCRIPTION = 100
_LEN_MAX_FIELD_VALUE = 30


def create(data: dict) -> List[Product]:

    validate_all_fields_product(data)
    return save(Product(id=str(uuid4()), name=data['name'], description=data['description'], value=data['value']))


def get() -> List:
    return Product.query.all()


def get_by_id(_product_id: str) -> Product:
    return Product.query.get(_product_id)


def update(_product_id: str, data: dict) -> Product:
    validate_all_fields_product(data)
    _product = get_by_id(_product_id)
    _product.name = data.get('name')
    _product.description = data.get('description')
    _product.value = data.get('value')
    commit()
    return _product


def delete_product(_product_id: str) -> NoReturn:
    Product.query.filter_by(id=_product_id).delete()
    commit()


def update_product_with_category(_product_id: str, _category_id: str) -> dict:
    _product = get_by_id(_product_id)
    _category = get_by_id_category(_category_id)
    _product.fk_category.append(_category)
    commit()
    _product_serialize = ProductSchemaMa.dump(_product)
    _product_serialize.update({'category_id': _category_id})
    return _product_serialize


def name_validate(name: str):
    if not name or len(name) > _LEN_MAX_FIELD_NAME:
        raise BadRequestException(msg=f"Name field cannot be empty or exceed "
                                      f"{_LEN_MAX_FIELD_NAME} limit of characters")


def description_validate(description: str):
    if not description or len(description) > _LEN_MAX_FIELD_DESCRIPTION:
        raise BadRequestException(msg=f"Description field cannot be empty or exceed "
                                      f"{_LEN_MAX_FIELD_DESCRIPTION} limit of characters")


def value_validate(value: str):
    if not value or len(value) > _LEN_MAX_FIELD_VALUE:
        raise BadRequestException(msg=f"Value field cannot be empty or exceed "
                                      f"{_LEN_MAX_FIELD_VALUE} limit of characters")
    if findall('[a-zA-Z!@#$%¨&*()`´^~:,<>?}{]', value):
        raise BadRequestException(msg="The field value, must be represented by a float number")


def validate_all_fields_product(data):
    value_validate(data['value'])
    name_validate(data['name'])
    description_validate(data['description'])
