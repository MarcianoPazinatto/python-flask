from flask import Blueprint, jsonify, request
from typing import Tuple
from app.domains.category.schema import CategorySchema
from app.domains.category.action import \
    create as create_category, \
    get as get_categories, \
    get_by_id as get_by_id_category,\
    update as update_category, delete_category

CategorySchemaMa = CategorySchema()
app_category = Blueprint('app.category', __name__)


@app_category.route('/category', methods=['POST'])
def post() -> Tuple:
    payload = request.get_json()
    category = create_category(payload)
    return CategorySchemaMa.dump(category), 201


@app_category.route('/categories', methods=['GET'])
def get() -> Tuple:
    return jsonify([CategorySchemaMa.dump(category) for category in get_categories()]), 200


@app_category.route('/category/<id>', methods=['GET'])
def get_by_id(id: str) -> Tuple:
    category = get_by_id_category(id)
    return CategorySchemaMa.dump(category), 200


@app_category.route('/category/<id>', methods=['PATCH'])
def patch(id:str) -> Tuple:
    payload = request.get_json()
    category = update_category(id, payload)
    return CategorySchemaMa.dump(category), 200


@app_category.route('/category/<id>', methods=['DELETE'])
def delete(id: str) -> Tuple:
    delete_category(id)
    return jsonify({}), 204
