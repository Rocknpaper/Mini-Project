from flask_restful import Resource, request
from json import loads
from myproject.models.employeeWorkDetails import EmployeeWorkDetails
from myproject.models.employeeLogin import EmployeeLogin
from myproject.models.departments import Departments
from myproject.helper.helpers import getPosition

class EmployeeWorkDetailsApi(Resource):
    def post(self, empID):
        body = request.get_json()
        employee = EmployeeLogin.objects(_id=empID).first()
        if employee != None:
            try:
                body["_id"] = empID
                dept = Departments.objects(_id=body["departmentId"]).first()

                if dept != None:
                    body["position"] = [getPosition(dept.departmentName)]
                    EmployeeWorkDetails(**body).save()
                    return {"Status": "OK"}, 200
            except Exception as e:
                return {"Status": "Failed", "Exception": str(e)}, 500
        else:
            return {"employee": "Not Found"}, 404

    def get(self, empID):
        employee = EmployeeLogin.objects(_id=empID).first()
        if employee != None:
            emp = EmployeeWorkDetails.objects(_id=empID)
            data = loads(emp.to_json())
            return data, 200

        else:
            return{"employee": "Not Found"}, 404
        


