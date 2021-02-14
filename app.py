from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

# local imports
from utils.routes import initialize_routes
from db import initialize_db

# dotenv file loading
load_dotenv()

app = Flask(__name__)
api = Api(app)
jwt = JWTManager(app)

# config
app.config['MONGODB_DB'] = 'brainy'
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
app.secret_key = os.getenv('SESSION_SECRET_KEY')

# initialize_db
initialize_db(app)

# initializing routes
initialize_routes(api)



if __name__ == '__main__':
    app.run(debug=True)