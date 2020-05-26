from datetime import date
from myproject import db

class EmployeePersonal(db.Document):
    _id = db.StringField(required=True)
    employeeDOB = db.DateTimeField(required=True)
    employeeMobileNo = db.ListField(required=True)
    employeeAddress = db.StringField(required=True, max_length=120)
    employeeJoindate = db.DateTimeField(required=True)

    meta = {
        "indexes": ["employeeJoindate"]
    }

    def calculateYears(self, born):
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))