from flask_restful import Resource, request
from werkzeug.security import generate_password_hash
from json import dumps, loads
from myproject.models.employeeLogin import EmployeeLogin


class EmployeeLoginApi(Resource):

    def get(self):
        resp = []
        employees = EmployeeLogin.objects()
        if employees:
            for employee in employees:
                data = employee.to_json()
                data = loads(data)
                # data = dumps(data, indent=2)
                resp.append(data)
            return {"employees": resp}, 200
        else:
            return {"employees": None}, 404

    def post(self):
        body = request.get_json()
        try:
            body["employeePassword"] = generate_password_hash(body["employeePassword"])
            EmployeeLogin(**body).save()
            return {"Status": "OK"}, 200
        except Exception as e:
            return {"Status": "Falied", "Execption": str(e)}, 500