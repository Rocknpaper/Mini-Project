from myproject import db

class EmployeePastTeams(db.EmbeddedDocument):
    _id = db.StringField(required=True)
    joinedTeam = db.DateTimeField(required=True)
    leftTeam = db.DateTimeField(default=None)