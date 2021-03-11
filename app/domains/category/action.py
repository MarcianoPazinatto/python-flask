from app.domains.category.model import Category
from database.repository import commit, save
from uuid import uuid4
from typing import List, NoReturn


def create(data: dict) -> List[Category]:
    return save(Category(id=str(uuid4()), name=data['name'], description=data['description']))


def get() -> List:
    return Category.query.all()


def get_by_id(_category_id: str) -> Category:
    return Category.query.get(_category_id)


def update(_category_id: str, data: dict) -> Category:
    _category = get_by_id(_category_id)
    _category.name = data.get('name')
    _category.description = data.get('description')
    commit()
    return _category


def delete_category(_category_id: str) -> NoReturn:
    Category.query.filter_by(id=_category_id).delete()
    commit()
