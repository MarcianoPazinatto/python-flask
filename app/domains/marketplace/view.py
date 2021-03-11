from flask import Blueprint, jsonify, request
from typing import Tuple
from app.domains.marketplace.schema import MarketplaceSchema
from app.domains.marketplace.action import \
    create as create_marketplace, \
    get as get_marketplaces, \
    get_by_id as get_by_id_marketplace,\
    update as update_marketplace, delete_marketplace

MarketplaceMa = MarketplaceSchema()
app_marketplace = Blueprint('app.marketplace', __name__)


@app_marketplace.route('/marketplace', methods=['POST'])
def post() -> Tuple:
    payload = request.get_json()
    marketplace = create_marketplace(payload)
    return MarketplaceMa.dump(marketplace), 201


@app_marketplace.route('/marketplaces', methods=['GET'])
def get() -> Tuple:
    return jsonify([MarketplaceMa.dump(marketplace) for marketplace in get_marketplaces()]), 200


@app_marketplace.route('/marketplace/<id>', methods=['GET'])
def get_by_id(id: str) -> Tuple:
    marketplace = get_by_id_marketplace(id)
    return MarketplaceMa.dump(marketplace), 200


@app_marketplace.route('/marketplace/<id>', methods=['PATCH'])
def patch(id:str) -> Tuple:
    payload = request.get_json()
    marketplace = update_marketplace(id, payload)
    return MarketplaceMa.dump(marketplace), 200


@app_marketplace.route('/marketplace/<id>', methods=['DELETE'])
def delete(id: str) -> Tuple:
    delete_marketplace(id)
    return jsonify({}), 204
