from flask_bcrypt import generate_password_hash, check_password_hash


# local imports
from db import db



class User(db.Document):
    username = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)
    phone_number = db.StringField(required=True)
    isActivated = db.BooleanField(default=False)
    isDriver = db.BooleanField(default=False)


    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf-8')

    def check_password(self, password):
        return check_password_hash(self.password, password)