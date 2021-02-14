from flask_restful import Resource, request
from flask import session
from marshmallow import ValidationError
from flask_jwt_extended import create_access_token
from mongoengine.errors import NotUniqueError, DoesNotExist
import datetime


# local imports
from models.auth import User
from schema.user import UserSignupSchema, UserLoginSchema, ConfirmUser
from utils.error import check_error
from utils.send_sms import sendOtp


# constant variables
USER_SIGNUP_SCHEMA = UserSignupSchema()
USER_LOGIN_SCHEMA = UserLoginSchema()
CONFIRM_USER = ConfirmUser()

# TODO: Validate users phone number to check if correct

class SignUp(Resource):
    @classmethod
    def post(cls):
        try:
            data = USER_SIGNUP_SCHEMA.load(request.get_json())
            user = User(**data)
            user.hash_password()
            user.save()
            sendOtp(user.username, user.phone_number, user.id)
          

            return {'Message': 'User Created'}, 200
        except ValidationError as e:
            print(e)
            return check_error(str(e))
        except NotUniqueError:
            return {'Message': 'User already exist'}, 500



class Login(Resource):
    @classmethod
    def post(cls):
        try:
            data = USER_LOGIN_SCHEMA.load(request.get_json())
            username = User.objects.get(username=data['username'])
            password = username.check_password(data['password'])
           
            if not password:
                return {'Message': 'Password is in-correct'}, 400

            expires = datetime.timedelta(minutes=10)
            token = create_access_token(identity=str(username.id), expires_delta=expires)

            return {'token': token}, 200
        except ValidationError as e:
            return check_error(str(e))
        except DoesNotExist:
            return {'Message': 'User does not exist'}, 404




class ConfirmUser(Resource):
    @classmethod
    def post(cls):
        try:
            data = CONFIRM_USER.load(request.get_json())
            if 'otp_key' in session:
                otp = session['otp_key']
                user_id = session['user_id']
                print('USER', user_id)
                if otp == data['otp']:
                    user = User.objects.get(pk=user_id)
                    user.update(isActivated=True)
                    return 'Valid OTP'
                else:
                    return 'Invalid OTP'
            return data
        except ValidationError as e:
            return check_error(str(e))