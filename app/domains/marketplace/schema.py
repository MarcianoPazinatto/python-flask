from database import ma

from app.domains.marketplace.model import Marketplace


class MarketplaceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Marketplace()
        include_fk = True

