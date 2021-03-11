from flask import Blueprint, jsonify, request
from typing import Tuple
from app.domains.seller.schema import SellerSchema
from app.domains.seller.action import \
    create as create_seller, \
    get as get_sellers, \
    get_by_id as get_by_id_seller,\
    update as update_seller, delete_seller

SellerSchemaMa = SellerSchema()
app_seller = Blueprint('app.seller', __name__)


@app_seller.route('/seller', methods=['POST'])
def post() -> Tuple:
    payload = request.get_json()
    seller = create_seller(payload)
    return SellerSchemaMa.dump(seller), 201


@app_seller.route('/sellers', methods=['GET'])
def get() -> Tuple:
    return jsonify([SellerSchemaMa.dump(seller) for seller in get_sellers()]), 200


@app_seller.route('/seller/<id>', methods=['GET'])
def get_by_id(id: str) -> Tuple:
    seller = get_by_id_seller(id)
    return SellerSchemaMa.dump(seller), 200


@app_seller.route('/seller/<id>', methods=['PATCH'])
def patch(id: str) -> Tuple:
    payload = request.get_json()
    seller = update_seller(id, payload)
    return SellerSchemaMa.dump(seller), 200


@app_seller.route('/seller/<id>', methods=['DELETE'])
def delete(id: str) -> Tuple:
    delete_seller(id)
    return jsonify({}), 204
