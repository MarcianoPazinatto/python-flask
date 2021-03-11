from app.domains.seller.model import Seller
from database.repository import commit, save
from uuid import uuid4
from typing import List, NoReturn


def create(data: dict) -> List[Seller]:
    return save(Seller(id=str(uuid4()), trade_name=data['trade_name'], company_name=data['company_name'],
                       cnpj=data['cnpj'], phone=data['phone'], email=data['email']))


def get() -> List:
    return Seller.query.all()


def get_by_id(_seller_id: str) -> Seller:
    return Seller.query.get(_seller_id)


def update(_seller_id: str, data: dict) -> Seller:
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
