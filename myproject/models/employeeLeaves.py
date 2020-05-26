from myproject import db
from myproject.helper.helpers import generateUniqueId

class LeaveTemplate(db.EmbeddedDocument):
    leave_id = db.StringField(required=True, default=generateUniqueId("V"))
    reason = db.StringField(required=True)
    leaveFrom = db.DateTimeField(required=True)
    leaveTo = db.DateTimeField(required=True)

class EmployeeLeaves(db.Document):
    _id = db.StringField(required=True)
    leaves = db.ListField(db.EmbeddedDocumentField(LeaveTemplate), required=True)

    