from flask_restful import Resource, request
from marshmallow import ValidationError

# local imports
from schema.delivery import DeliverySchema
from utils.error import check_error


# constant variables
DELIVERY_SCHEMA = DeliverySchema()


class Delivery(Resource):
    @classmethod
    def post(cls):
        try:
            data = DELIVERY_SCHEMA.load(request.get_json())
            return data
        except ValidationError as e:
            return check_error(str(e))
        