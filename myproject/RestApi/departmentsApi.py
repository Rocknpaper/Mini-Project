from flask_restful import Resource, request
from json import loads
from myproject.models.departments import Departments

class DepartmentsApi(Resource):
    def post(self):
        body = request.get_json()
        try:
            Departments(**body).save()
            return {"Status": "OK"}, 200
        except Exception as e:
            return {"Status": "Failed", "Exception": str(e)}, 500

    def get(self):
        depts = Departments.objects()
        if depts != None:
            resp = []
            for dept in depts:
                data = loads(dept.to_json())
                resp.append(data)

            return {"departments": resp}, 200

        else:
            return {"departments": "Not Found"}, 404