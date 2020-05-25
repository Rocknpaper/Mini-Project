from myproject import db

class Departments(db.Document):
    _id = db.StringField(primary_key=True, min_length=6, max_length=6)
    departmentName = db.StringField(required=True, unique=True)
    departmentHead = db.StringField(required=True)
