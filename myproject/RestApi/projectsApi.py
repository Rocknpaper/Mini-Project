from flask_restful import Resource, request
from myproject.models.project import Projects


class ProjectsApi(Resource):
    def post(self):
        body = request.get_json()
        try:
            Projects(**body).save()
            return {"Status": "OK"}
        except Exception as e:
            return {"Status": "Failed", "Exception": str(e)}