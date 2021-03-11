import uuid
from database import db

category_product = db.Table('category_product',
                            db.Column('product_id', db.String(36), db.ForeignKey('product.id')),
                            db.Column('category_id', db.String(36), db.ForeignKey('category.id')))

class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.String(36), default=str(uuid.uuid4()), primary_key=True, nullable=False, autoincrement=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    value = db.Column(db.Float(), nullable=False)
    fk_category = db.relationship('Category', secondary= category_product, back_populates='fk_product', lazy='joined')