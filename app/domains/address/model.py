import uuid
from database import db
from app.domains.seller.model import Seller


class Address(db.Model):
    __tablename__ = 'address'

    id = db.Column(db.String(36), default=str(uuid.uuid4()), primary_key=True, nullable=False, autoincrement=False)
    street = db.Column(db.String(100), nullable=False)
    number = db.Column(db.String(8), nullable=False)
    district = db.Column(db.String(100), nullable=False)
    cep = db.Column(db.String(8), nullable=False)
    complement = db.Column(db.String(100), nullable=True)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    seller_id = db.Column(db.String(36), db.ForeignKey('seller.id'), nullable=False)
    seller = db.relationship(Seller, back_populates='seller_address')


