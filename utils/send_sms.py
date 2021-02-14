from twilio.rest import Client
from dotenv import load_dotenv
from random import randrange
from flask import session
import os


# Enviromwent variables
load_dotenv()
ACCOUNT_SID = os.getenv('ACCOUNT_SID')
AUTH_TOKEN = os.getenv('AUTH_TOKEN')
MY_TWILIO= os.getenv('MY_TWILIO')

# Generating OTP
otp = randrange(100000, 999999)

# Sending OTP
def sendOtp(username, phone_number, id):
    session['otp_key'] = otp
    session['user_id'] = str(id)
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = f'Hello {username} this is your otp {otp}'
    send_msg =client.messages.create(to=phone_number, from_=MY_TWILIO, body=message)
