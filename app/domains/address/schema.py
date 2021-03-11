from database import ma

from app.domains.address.model import Address


class AddressSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Address()
        include_fk = True

