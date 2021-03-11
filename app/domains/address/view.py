from flask import Blueprint, jsonify, request
from typing import Tuple
from app.domains.address.schema import AddressSchema
from app.domains.address.action import \
    create as create_address, \
    get as get_addresses, \
    get_by_id as get_by_id_address,\
    update as update_address, delete_address

AddressSchemaMa = AddressSchema()
app_address = Blueprint('app.address', __name__)


@app_address.route('/address', methods=['POST'])
def post() -> Tuple:
    payload = request.get_json()
    address = create_address(payload)
    return AddressSchemaMa.dump(address), 201


@app_address.route('/addresses', methods=['GET'])
def get() -> Tuple:
    return jsonify([AddressSchemaMa.dump(address) for address in get_addresses()]), 200


@app_address.route('/address/<id>', methods=['GET'])
def get_by_id(id: str) -> Tuple:
    address = get_by_id_address(id)
    return AddressSchemaMa.dump(address), 200


@app_address.route('/address/<id>', methods=['PATCH'])
def patch(id:str) -> Tuple:
    payload = request.get_json()
    address = update_address(id, payload)
    return AddressSchemaMa.dump(address), 200


@app_address.route('/address/<id>', methods=['DELETE'])
def delete(id: str) -> Tuple:
    delete_address(id)
    return jsonify({}), 204
