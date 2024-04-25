from Backend.shared.ma import ma
from Backend.locations.models import Location

class LocationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Location

location_schema = LocationSchema()
locations_schema = LocationSchema(many=True)
