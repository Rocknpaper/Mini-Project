from datetime import date
from myproject import db

class EmployeePersonal(db.Document):
    _id = db.StringField(required=True)
    employeeDOB = db.DateTimeField(required=True)
    employeeSalary = db.FloatField(required=True)
    employeeJoindate = db.DateTimeField(required=True)
    apprasialsOverTheYears = db.StringField(default=None)

    meta = {
        "indexes": ["employeeJoindate"]
    }

    def calculateYears(self, born):
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))