from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)

# app.config.from_pyfile("settings.cfg")

db = MongoEngine(app)
from myproject.models.employeeLogin import EmployeeLogin


# Employee(
#     employeeName="Tharun Kumar A",
#     employeeUsername="tharun11",
#     employeeEmail = "tharun7@gmail.com",
#     employeePassword = "tharun77"
# ).save()

# emp = Employee.objects()

# for e in emp:

#     print(e.doesPasswordMatch("Hooooo"))



from myproject import RestApi


