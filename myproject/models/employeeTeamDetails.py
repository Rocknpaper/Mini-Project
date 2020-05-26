from myproject import db
from myproject.models.employeePastTeams import EmployeePastTeams

class EmployeeTeamDetails(db.Document):
    _id = db.StringField(required=True)
    teamsWorked = db.ListField(db.EmbeddedDocumentField(EmployeePastTeams), default=None)
    projectsWorked = db.ListField()
    departmentHead = db.BooleanField(default=False)
