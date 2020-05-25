from flask_restful import Resource, request
from myproject.models.departments import Departments

class DepartmentsApi(Resource):
    def post(self):
        body = request.get_json()
        try:
            Departments(**body).save()
            return {"Status": "OK"}, 200
        except Exception as e:
            return {"Status": "Failed", "Exception": str(e)}, 500