from myproject import db
from myproject.helper.helpers import generateUniqueId

class Teams(db.Document):
    _id = db.StringField(primary_key=True, default=generateUniqueId("T"))
    teamName = db.StringField(unique=True, required=True)
    teamLead = db.StringField(required=True)
    teamMembers = db.ListField(required=True, unique=True)
    projectsDone = db.ListField(required=True, unique=True)
    currentProject = db.StringField()

    meta = {
        "indexes": ["teamLead"]
    }
