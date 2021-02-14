from db import db



class DriverAgent(db.Document):
    driver_id = db.ObjectIdField()
    vehicle_type = db.StringField()
    location = db.StringField()
