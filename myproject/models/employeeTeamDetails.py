from myproject import db

class EmployeeTeamDetails(db.Document):
    _id = db.StringField(required=True)
    teamsWorked = db.ListField()
    projectsWorked = db.ListField()
    departmentHead = db.BooleanField(default=False)
