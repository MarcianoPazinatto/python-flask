import uuid
from database import db


class Seller(db.Model):
    __tablename__ = 'seller'

    id = db.Column(db.String(36), default=str(uuid.uuid4()), primary_key=True, nullable=False, autoincrement=False)
    trade_name = db.Column(db.String(100), nullable=False)
    company_name = db.Column(db.String(100), nullable=False)
    cnpj = db.Column(db.String(14), nullable=False)
    phone = db.Column(db.String(16), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    seller_address = db.relationship('Address', back_populates='seller', uselist=False)
