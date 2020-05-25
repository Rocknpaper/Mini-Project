from werkzeug.security import check_password_hash
from myproject.helper.helpers import generateUniqueId
from myproject import db
    

class EmployeeLogin(db.Document):
    _id = db.StringField(primaryKey=True, default=generateUniqueId("E"))
    employeeName = db.StringField(required=True, max_length=32)
    employeeUsername = db.StringField(requird=True, unique=True, max_length=12)
    employeeEmail = db.EmailField(required=True, unique=True)
    employeePassword = db.StringField(required=True)

    meta = {
        "indexes": ["employeeEmail", "employeeUsername"]
    }


    def doesPasswordMatch(self, password):
        return check_password_hash(self.employeePassword, password)






