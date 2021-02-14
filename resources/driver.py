from flask_restful import Resource, request



# local imports
from models.auth import User
from models.driver import DriverAgent

class Driver(Resource):
    @classmethod
    def post(cls, id):
        data = request.get_json()
        user = User.objects.get(pk=id)
        driver = DriverAgent()

        if user:
            driver.driver_id = user.id
            driver.vehicle_type = data['vehicle_type']
            driver.location = data['location']
            user.update(isDriver=True)
            driver.save()
        else:
            return 'User does not exist'
        return data
