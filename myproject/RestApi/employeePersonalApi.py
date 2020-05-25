from flask_restful import Resource, request
from json import loads
from myproject.models.employeePersonal import EmployeePersonal
from myproject.models.employeeLogin import EmployeeLogin
from myproject.helper.helpers import dateToString

class EmployeePersonalApi(Resource):
    def post(self, empID):
        body = request.get_json()
        try:
            emp = EmployeeLogin.objects(_id=empID).first()
            body["_id"] = emp._id
            if emp:
                EmployeePersonal(**body).save()
                return {"Status": "OK"}, 200
            else:
                return {"Employee": "Not Found"}, 404

        except Exception as e:
            return{"Status": "Failed", "Exception": str(e)}, 400

    def get(self, empID):
        emp = EmployeeLogin.objects(_id=empID).first()
        if emp:
            try:
                employee = EmployeePersonal.objects(_id=emp._id).first()
                data = loads(employee.to_json())
                data["employeeAge"] = employee.calculateYears(employee["employeeDOB"])
                data["workingFor"] = employee.calculateYears(employee["employeeJoindate"])
                DOB = dateToString(employee, "employeeDOB")
                Jdate = dateToString(employee, "employeeJoindate")
                data["employeeDOB"] = DOB
                data["employeeJoindate"] = Jdate
                return data, 200
            except Exception as e:
                return {"Status": "Falied", "Execption": str(e)}, 500

        else:
            return {"Employee": "Not Found"}, 404

        



