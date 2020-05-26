from myproject import db

class ApprasialsandAllowance(db.EmbeddedDocument):
    year = db.StringField(required=True, max_length=4)
    amount = db.FloatField(required=True)


class EmployeeSalary(db.Document):
    _id = db.StringField(required=True)
    employeeSalary = db.FloatField(required=True)
    apprasialsOverTheYears = db.ListField(db.EmbeddedDocumentField(ApprasialsandAllowance), default=None)
    allowancesOverTheYears = db.ListField(db.EmbeddedDocumentField(ApprasialsandAllowance), default=None)
    employeePF = db.IntField(required=True)
    employeeAllowances = db.FloatField(required=True)
