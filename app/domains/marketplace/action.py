from app.domains.marketplace.model import Marketplace
from database.repository import commit, save
from uuid import uuid4
from typing import List, NoReturn


def create(data: dict) -> List[Marketplace]:
    return save(Marketplace(id=str(uuid4()), name=data['name'], description=data['description'], site=data['site'],
                            phone=data['phone'], email=data['email'], contact_name=data['contact_name']))


def get() -> List:
    return Marketplace.query.all()


def get_by_id(_marketplace_id: str) -> Marketplace:
    return Marketplace.query.get(_marketplace_id)


def update(_marketplace_id: str, data: dict) -> Marketplace:
    _marketplace = get_by_id(_marketplace_id)
    _marketplace.name = data.get('name')
    _marketplace.description = data.get('description')
    _marketplace.site = data.get('site')
    _marketplace.phone = data.get('phone')
    _marketplace.email = data.get('email')
    _marketplace.contact_name = data.get('contact_name')
    commit()
    return _marketplace


def delete_marketplace(_marketplace_id: str) -> NoReturn:
    Marketplace.query.filter_by(id=_marketplace_id).delete()
    commit()
