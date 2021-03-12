from app.domains.address.model import Address
from database.repository import commit, save
from uuid import uuid4
from typing import List, NoReturn


def create(data: dict) -> List[Address]:
    return save(Address(id=str(uuid4()), street=data['street'], number=data['number'], district=data['district'],
                        zip_code=data['zip_code'], complement=data['complement'], city=data['city'], state=data['state'],
                        country=data['country'], seller_id=data['seller_id']))


def get() -> List:
    return Address.query.all()


def get_by_id(_address_id: str) -> Address:
    return Address.query.get(_address_id)


def update(_address_id: str, data: dict) -> Address:
    _address = get_by_id(_address_id)
    _address.street = data.get('street')
    _address.number = data.get('number')
    _address.district = data.get('district')
    _address.zip_code = data.get('zip_code')
    _address.complement = data.get('complement')
    _address.city = data.get('city')
    _address.state = data.get('state')
    _address.country = data.get('country')
    commit()
    return _address


def delete_address(_address_id: str) -> NoReturn:
    Address.query.filter_by(id=_address_id).delete()
    commit()