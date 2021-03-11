from database import ma

from app.domains.seller.model import Seller


class SellerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Seller()
    include_fk = True

