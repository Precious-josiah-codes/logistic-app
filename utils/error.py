# constant variables
PASSWORD_REQUIRED = "'password': ['Missing data for required field.']"
PHONE_NUMBER_REQUIRED = "'phone_number': ['Missing data for required field.']}"
USERNAME_REQUIRED = "'name': ['Missing data for required field.']"
DESTINATION = "'destination': ['Missing data for required field.']"
RECIEVER_NAME = "'reciever_name': ['Missing data for required field.']"
RECIEVER_NUMBER = "'reciever_number': ['Missing data for required field.']"
PICKUP_RIDE = "'pickup_ride': ['Missing data for required field.']"
OTP_REQUIRED = "'otp': ['Missing data for required field.']"
INVALID_OTP = "{'otp': ['Not a valid integer.']}"


error_message = {
    'PasswordRequired': {
        'message': 'Password is required',
        'status': 400
    },
    'PhoneNumberRequired': {
        'message': 'Phone number is required',
        'status': 400
    },
    'UserNameRequired': {
        'message': 'Username is required',
        'status': 400
    },
    'DestinationRequired': {
        'message': 'Destination is required',
        'status': 400
    },
    'RecieverNameRequired': {
        'message': 'Reciever name is required',
        'status': 400
    },
    'RecieverNumberRequired': {
        'message': 'Reciever number is required',
        'status': 400
    },
    'PickupRideRequired': {
        'message': 'Pickup ride is required',
        'status': 400
    },
    'OtpRequired': {
        'message': 'OTP is required',
        'status': 400
    },
    'InvalidOtp': {
        'message': 'Invalid OTP',
        'status': 400
    }
}



def check_error(err_msg):
    if PASSWORD_REQUIRED in err_msg:
        return error_message['PasswordRequired']
    elif PHONE_NUMBER_REQUIRED in err_msg:
        return error_message['PhoneNumberRequired']
    elif USERNAME_REQUIRED in err_msg:
        return error_message['UsernameRequired']
    elif DESTINATION in err_msg:
        return error_message['DestinationRequired']
    elif RECIEVER_NAME in err_msg:
        return error_message['RecieverNameRequired']
    elif RECIEVER_NUMBER in err_msg:
        return error_message['RecieverNumberRequired']
    elif PICKUP_RIDE in err_msg:
        return error_message['PickupRideRequired']
    elif OTP_REQUIRED in err_msg:
        return error_message['OtpRequired']
    elif INVALID_OTP in err_msg:
        return error_message['InvalidOtp']
    else:
        return err_msg