from marshmallow import Schema, fields



class DeliverySchema(Schema):
    pickup = fields.Str()
    destination = fields.Str(required=True)
    reciever_name = fields.Str(required=True)
    reciever_number = fields.Str(required=True)
    pickup_ride = fields.Str(required=True)

