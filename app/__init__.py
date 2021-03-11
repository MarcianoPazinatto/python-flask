from flask import Flask, json

from werkzeug.exceptions import HTTPException, InternalServerError

from app.domains.category.view import app_category
from app.domains.address.view import app_address
from app.domains.seller.view import app_seller
from app.domains.marketplace.view import app_marketplace
from app.domains.product.view import app_product


from database import db, migrate


def create_app():
    app = Flask(__name__)
    app.config.from_object('settings')
    db.init_app(app)
    migrate.init_app(app, db)
    _register_blueprint(app)
    _register_error_handler(app)
    return app


def _register_blueprint(app):
   app.register_blueprint(app_category)
   app.register_blueprint(app_seller)
   app.register_blueprint(app_product)
   app.register_blueprint(app_marketplace)
   app.register_blueprint(app_address)


def _handle_default_exception(e):
    response = e.get_response()
    code = e.code
    description = e.description
    response.data = get_data(code, description)
    response.content_type = "application/json"
    return response, code


def get_data(code, description):
    return json.dumps({
        'code': code,
        'message': description,
    })


def _handle_internal_server_error_exception(e):
    response = e.get_response()
    code = 500
    description = 'Sorry, we cant process request. Try again.'
    response.data = get_data(code, description)
    response.content_type = "application/json"
    return response, code


def _register_error_handler(app):
    app.register_error_handler(HTTPException, _handle_default_exception)
    app.register_error_handler(InternalServerError, _handle_internal_server_error_exception)
