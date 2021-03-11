from flask import Blueprint, jsonify, request
from typing import Tuple
from app.domains.product.schema import ProductSchema
from app.domains.product.action import \
    create as create_product, \
    get as get_products, \
    get_by_id as get_by_id_product,\
    update as update_product, delete_product

ProductMa = ProductSchema()
app_product = Blueprint('app.product', __name__)


@app_product.route('/product', methods=['POST'])
def post() -> Tuple:
    payload = request.get_json()
    product = create_product(payload)
    return ProductMa.dump(product), 201


@app_product.route('/products', methods=['GET'])
def get() -> Tuple:
    return jsonify([ProductMa.dump(product) for product in get_products()]), 200


@app_product.route('/product/<id>', methods=['GET'])
def get_by_id(id: str) -> Tuple:
    product = get_by_id_product(id)
    return ProductMa.dump(product), 200


@app_product.route('/product/<id>', methods=['PATCH'])
def patch(id:str) -> Tuple:
    payload = request.get_json()
    product = update_product(id, payload)
    return ProductMa.dump(product), 200


@app_product.route('/product/<id>', methods=['DELETE'])
def delete(id: str) -> Tuple:
    delete_product(id)
    return jsonify({}), 204
