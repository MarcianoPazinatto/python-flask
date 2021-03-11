from database import ma

from app.domains.product.model import Product


class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product()
        include_fk = True

