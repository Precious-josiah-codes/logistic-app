from resources.auth import SignUp, Login, ConfirmUser
from resources.delivery import Delivery
from resources.pickup import Pickup
from resources.driver import Driver


def initialize_routes(api):
    api.add_resource(SignUp, '/api/auth/register_user')
    api.add_resource(Login, '/api/auth/login_user')
    api.add_resource(Delivery, '/api/delivery')
    api.add_resource(Pickup, '/api/pickup')
    api.add_resource(ConfirmUser, '/api/confirm_user')
    api.add_resource(Driver, '/api/<id>/driver')