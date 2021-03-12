import uuid

import requests
from sqlalchemy.orm import validates

from app.domains.seller.model import Seller
from app.exceptions import BadRequestException
from database import db

_LEN_MAX_FIELD_STREET = 100
_LEN_MAX_FIELD_NUMBER = 8
_LEN_MAX_FIELD_DISTRICT = 100
_LEN_MAX_FIELD_COMPLEMENT = 100
_LEN_MAX_FIELD_CITY = 100
_LEN_MAX_FIELD_STATE = 100
_LEN_MAX_FIELD_COUNTRY = 100


class Address(db.Model):
    __tablename__ = 'address'

    id = db.Column(db.String(36), default=str(uuid.uuid4()), primary_key=True, nullable=False, autoincrement=False)
    street = db.Column(db.String(100), nullable=False)
    number = db.Column(db.String(8), nullable=False)
    district = db.Column(db.String(100), nullable=False)
    zip_code = db.Column(db.String(8), nullable=False)
    complement = db.Column(db.String(100), nullable=True)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    seller_id = db.Column(db.String(36), db.ForeignKey('seller.id'), nullable=False)
    seller = db.relationship(Seller, back_populates='seller_address')

    @validates('street')
    def street_validate(self, key, street: str):
        if not street or len(street) > _LEN_MAX_FIELD_STREET:
            raise BadRequestException(msg=f"Name field cannot be empty or exceed "
                                          f"{_LEN_MAX_FIELD_STREET} limit of characters.")
        return street

    @validates('number')
    def number_validate(self, key, number: str):
        if not number or len(number) > _LEN_MAX_FIELD_NUMBER:
            raise BadRequestException(msg=f"Number field cannot be empty or exceed "
                                          f"{_LEN_MAX_FIELD_NUMBER} limit of characters.")
        return number

    @validates('district')
    def district_validate(self, key, district: str):
        if not district or len(district) > _LEN_MAX_FIELD_DISTRICT:
            raise BadRequestException(msg=f"District field cannot be empty or exceed "
                                          f"{_LEN_MAX_FIELD_DISTRICT} limit of characters.")
        return district

    @validates('complement')
    def complement_validate(self, key, complement: str):
        if not complement or len(complement) > _LEN_MAX_FIELD_COMPLEMENT:
            raise BadRequestException(msg=f"Complement field cannot be empty or exceed "
                                          f"{_LEN_MAX_FIELD_COMPLEMENT} limit of characters.")
        return complement

    @validates('city')
    def city_validate(self, key, city: str):
        if not city or len(city) > _LEN_MAX_FIELD_CITY:
            raise BadRequestException(msg=f"City field cannot be empty or exceed "
                                          f"{_LEN_MAX_FIELD_CITY} limit of characters.")
        return city

    @validates('state')
    def state_validate(self, key, state: str):
        if not state or len(state) > _LEN_MAX_FIELD_STATE:
            raise BadRequestException(msg=f"State field cannot be empty or exceed "
                                          f"{_LEN_MAX_FIELD_STATE} limit of characters.")
        return state

    @validates('country')
    def country_validate(self, key, country: str):
        if not country or len(country) > _LEN_MAX_FIELD_COUNTRY:
            raise BadRequestException(msg=f"Country field cannot be empty or exceed "
                                          f"{_LEN_MAX_FIELD_COUNTRY} limit of characters.")
        return country

    @validates('zip_code')
    def zip_code_validate(self, key, zip_code: str):
        req = requests.get('https://viacep.com.br/ws/{}/json'.format(zip_code))
        if req.status_code == 200:
            return zip_code
        raise BadRequestException(msg="Zip code incorrect.")
