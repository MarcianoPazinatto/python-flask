import uuid

from email_validator import validate_email, EmailNotValidError
from sqlalchemy.orm import validates
from validate_docbr.CNPJ import CNPJ

from app.exceptions import BadRequestException, UnprocessableException
from database import db

cnpj_validate = CNPJ()
_LEN_MAX_FIELD_TRADE_NAME = 100
_LEN_MAX_FIELD_COMPANY_NAME = 100
_LEN_MAX_FIELD_PHONE = 16


class Seller(db.Model):
    __tablename__ = 'seller'

    id = db.Column(db.String(36), default=str(uuid.uuid4()), primary_key=True, nullable=False, autoincrement=False)
    trade_name = db.Column(db.String(100), nullable=False)
    company_name = db.Column(db.String(100), nullable=False)
    cnpj = db.Column(db.String(14), nullable=False)
    phone = db.Column(db.String(16), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    seller_address = db.relationship('Address', back_populates='seller', uselist=False)

    @validates('trade_name')
    def trade_name_validate(self, key, trade_name: str):
        if not trade_name or len(trade_name) > _LEN_MAX_FIELD_TRADE_NAME:
            raise BadRequestException(msg=f"Company name field cannot be empty or exceed "
                                          f"{_LEN_MAX_FIELD_TRADE_NAME} limit of characters")
        return trade_name

    @validates('company_name')
    def company_name_validate(self, key, company_name: str):
        if not company_name or len(company_name) > _LEN_MAX_FIELD_COMPANY_NAME:
            raise BadRequestException(msg=f"Company name field cannot be empty or exceed "
                                          f"{_LEN_MAX_FIELD_COMPANY_NAME} limit of characters")
        return company_name

    @validates('cnpj')
    def cnpj_validate(self, key, cnpj: str):
        if not cnpj_validate.validate(cnpj):
            raise BadRequestException(msg="CNPJ invalid")
        return cnpj

    @validates('phone')
    def phone_validate(self, key, phone: str):
        if not phone or len(phone) > _LEN_MAX_FIELD_PHONE or not phone.isnumeric():
            raise BadRequestException(msg=f"Phone field cannot be empty, exceed "
                                          f"{_LEN_MAX_FIELD_PHONE} limit of characters, must contain only numbers")
        return phone

    @validates('email')
    def email_validate(self, key, email: str):
        try:
            validate_email(email)
            return email
        except EmailNotValidError as ex:
            raise UnprocessableException(msg=str(ex))
