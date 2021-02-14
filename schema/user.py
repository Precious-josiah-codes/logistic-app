from marshmallow import Schema, fields



class UserSignupSchema(Schema):
    class Meta:
        load_only = ('password',)

    username = fields.Str(required=True)
    password = fields.Str(required=True)
    phone_number = fields.Str(required=True)

class UserLoginSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)

class ConfirmUser(Schema):
    otp = fields.Int(required=True)