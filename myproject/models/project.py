from myproject import db
from myproject.helper.helpers import generateUniqueId

class Projects(db.Document):
    _id = db.StringField(primary_key=True, default=generateUniqueId("P"))
    projectName = db.StringField(required=True, max_length=64)
    projectFrom = db.StringField(required=True)
    projectDeadLine = db.DateTimeField(required=True)
    startDate = db.DateTimeField(required=True)
    endDate = db.DateTimeField(default=None)
    doneBy = db.ListField(required=True, unique=True)
