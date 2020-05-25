from myproject import db
# from myproject.helper.helpers import HelperFunctions

class EmployeeWorkDetails(db.Document):
    _id = db.StringField(required=True)
    departmentId = db.StringField(required=True)
    position = db.ListField(unique=True)
    teamId = db.StringField(required=True)
    teamLeader = db.BooleanField(default=False)
    



