from app.domains.product.model import Product
from database.repository import commit, save
from uuid import uuid4
from typing import List, NoReturn


def create(data: dict) -> List[Product]:
    return save(Product(id=str(uuid4()), name=data['name'], description=data['description'], value=data['value']))


def get() -> List:
    return Product.query.all()


def get_by_id(_product_id: str) -> Product:
    return Product.query.get(_product_id)


def update(_product_id: str, data: dict) -> Product:
    _product = get_by_id(_product_id)
    _product.name = data.get('name')
    _product.description = data.get('description')
    _product.value = data.get('value')
    commit()
    return _product


def delete_product(_product_id: str) -> NoReturn:
    Product.query.filter_by(id=_product_id).delete()
    commit()
