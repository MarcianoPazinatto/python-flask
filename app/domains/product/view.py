from typing import Tuple

from flask import Blueprint, jsonify, request

from app.domains.category.schema import CategorySchema
from app.domains.product.action import \
    create as create_product, \
    get as get_products, \
    get_by_id as get_by_id_product, get_all_products, \
    update as update_product, delete_product, update_product_with_category, \
    get_by_all_values, get_by_category_name_only
from app.domains.product.schema import ProductSchema

CategoryMa = CategorySchema()
ProductMa = ProductSchema()
app_product = Blueprint('app.product', __name__)


@app_product.route('/product', methods=['POST'])
def post() -> Tuple:
    payload = request.get_json()
    product = create_product(payload)
    return ProductMa.dump(product), 201


@app_product.route('/products', methods=['GET'])
def get() -> Tuple:
    payload = request.get_json()
    if payload is None:
        return jsonify([ProductMa.dump(product) for product in get_all_products()]), 200
    if payload['category_name'] != "" and payload['name'] != "" and payload['description'] != "" and payload[
        'value'] != "":
        return jsonify([ProductMa.dump(product) for product in get_by_all_values(payload)]), 200
    elif payload['category_name'] != "" and payload['name'] == "" and payload['description'] == "" and payload[
        'value'] == "":
                return jsonify([ProductMa.dump(product) for product in get_by_category_name_only(payload)]), 200
    elif payload['category_name'] == "" and payload['name'] != "" or payload['description'] != "" or payload[
        'value'] != "":
        filtered_products = get_products(payload)
        return jsonify([ProductMa.dump(product) for product in filtered_products]), 200
    elif payload['category_name'] == "" and payload['name'] == "" and payload['description'] == "" and payload[
        'value'] == "":
        return jsonify([ProductMa.dump(product) for product in get_all_products()]), 200


@app_product.route('/product/<id>', methods=['GET'])
def get_by_id(id: str) -> Tuple:
    product = get_by_id_product(id)
    return ProductMa.dump(product), 200


@app_product.route('/product/<id>', methods=['PATCH'])
def patch(id: str) -> Tuple:
    payload = request.get_json()
    product = update_product(id, payload)
    return ProductMa.dump(product), 200


@app_product.route('/product/<id>', methods=['DELETE'])
def delete(id: str) -> Tuple:
    delete_product(id)
    return jsonify({}), 204


@app_product.route('/product/<_product_id>/category/<_category_id>', methods=['POST'])
def create_product_with_category(_product_id: str, _category_id: str) -> tuple:
    _product = update_product_with_category(_product_id, _category_id)
    return ProductMa.dump(_product), 200

