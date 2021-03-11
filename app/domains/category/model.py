import uuid
from database import db
from app.domains.product.model import category_product

class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.String(36), default=str(uuid.uuid4()), primary_key=True, nullable=False, autoincrement=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    fk_product = db.relationship('Product', secondary=category_product, back_populates='fk_category', lazy='joined')