from email_validator import validate_email, EmailNotValidError
from validate_docbr.CNPJ import CNPJ

from app.exceptions import BadRequestException, UnprocessableException
from database.repository import commit, save
from uuid import uuid4
from typing import List, NoReturn
from app.domains.seller.model import Seller

cnpj_validator = CNPJ()
_LEN_MAX_FIELD_TRADE_NAME = 100
_LEN_MAX_FIELD_COMPANY_NAME = 100
_LEN_MAX_FIELD_PHONE = 16


def create(data: dict) -> List[Seller]:
    validate_all_fields(data)
    return save(Seller(id=str(uuid4()), trade_name=data['trade_name'], company_name=data['company_name'],
                       cnpj=data['cnpj'], phone=data['phone'], email=data['email']))


def get() -> List:
    return Seller.query.all()


def get_by_id(_seller_id: str) -> Seller:
    return Seller.query.get(_seller_id)


def update(_seller_id: str, data: dict) -> Seller:
    validate_all_fields(data)
    _seller = get_by_id(_seller_id)
    _seller.trade_name = data.get('trade_name')
    _seller.company_name = data.get('company_name')
    _seller.cnpj = data.get('cnpj')
    _seller.phone = data.get('phone')
    _seller.email = data.get('email')
    commit()
    return _seller


def delete_seller(_seller_id: str) -> NoReturn:
    Seller.query.filter_by(id=_seller_id).delete()
    commit()


def trade_name_validate(trade_name: str):
    if not trade_name or len(trade_name) > _LEN_MAX_FIELD_TRADE_NAME:
        raise BadRequestException(msg=f"Company name field cannot be empty or exceed "
                                      f"{_LEN_MAX_FIELD_TRADE_NAME} limit of characters")


def company_name_validate(company_name: str):
    if not company_name or len(company_name) > _LEN_MAX_FIELD_COMPANY_NAME:
        raise BadRequestException(msg=f"Company name field cannot be empty or exceed "
                                      f"{_LEN_MAX_FIELD_COMPANY_NAME} limit of characters")


def cnpj_validate(cnpj: str):
    if not cnpj_validator.validate(cnpj):
        raise BadRequestException(msg="CNPJ invalid")


def phone_validate(phone: str):
    if not phone or len(phone) > _LEN_MAX_FIELD_PHONE or not phone.isnumeric():
        raise BadRequestException(msg=f"Phone field cannot be empty, exceed "
                                      f"{_LEN_MAX_FIELD_PHONE} limit of characters, must contain only numbers")


def email_validate(email: str):
    try:
        validate_email(email)
        return email
    except EmailNotValidError as ex:
        raise UnprocessableException(msg=str(ex))


def validate_all_fields(data):
    company_name_validate(data['company_name'])
    cnpj_validate(data['cnpj'])
    trade_name_validate(data['trade_name'])
    phone_validate(data['phone'])
    email_validate(data['email'])
