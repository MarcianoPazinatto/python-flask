from typing import List, NoReturn
from uuid import uuid4

from app.domains.category.action import get_by_id as get_by_id_category
from app.domains.category.model import Category
from app.domains.category.schema import CategorySchema
from app.domains.product.model import Product, category_product
from app.domains.product.schema import ProductSchema
from database.repository import commit, save

CategorySchemaMa = CategorySchema()
ProductSchemaMa = ProductSchema()


def create(data: dict) -> List[Product]:
    return save(Product(id=str(uuid4()), name=data['name'], description=data['description'], value=data['value']))


def get_all_products() -> List:
    return Product.query.all()


def get(data: dict) -> List:
    if data['name'] != "" and data['description'] == "" and data['value'] == "":
        return Product.query.filter_by(name=data['name'])
    elif data['name'] == "" and data['description'] != "" and data['value'] == "":
        return Product.query.filter_by(description=data['description'])
    elif data['name'] == "" and data['description'] == "" and data['value'] != "":
        return Product.query.filter_by(value=data['value'])
    elif data['name'] != "" and data['description'] != "" and data['value'] != "":
        return Product.query.filter_by(name=data['name']).filter_by(description=data['description']).filter_by(
            value=data['value'])


def get_by_all_values(data: dict) -> List:
    category = Category.query.filter_by(name=data['category_name']).first()
    category_serialize = CategorySchemaMa.dump(category)
    product = Product.query.filter_by(name=data['name']).filter_by(description=data['description']).filter_by(
        value=data['value']).first()
    product_serialize = ProductSchemaMa.dump(product)
    return get_product_with_category_name(product_serialize, category_serialize)


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


def update_product_with_category(_product_id: str, _category_id: str) -> dict:
    _product = get_by_id(_product_id)
    _category = get_by_id_category(_category_id)
    _product.fk_category.append(_category)
    commit()
    _product_serialize = ProductSchemaMa.dump(_product)
    _product_serialize.update({'category_id': _category_id})
    return _product_serialize


def get_product_with_category_name(product_id: dict, category_id: dict) -> List:
    if not product_id or not category_id:
        return []
    return Product.query.join(category_product).join(Category).filter(
        (category_product.c.product_id == product_id['id']) &
        (category_product.c.category_id == category_id['id'])).all()


def get_by_category_name_only(data: dict) -> List:
    category = Category.query.filter_by(name=data['category_name']).first()
    category_serialize = CategorySchemaMa.dump(category)
    return get_category_name_with_auxiliar_table(category_serialize)


def get_category_name_with_auxiliar_table(category_id: dict) -> List:
    if not category_id:
        return []
    return Product.query.join(category_product).join(Category).filter(
        (category_product.c.category_id == category_id['id'])).all()
