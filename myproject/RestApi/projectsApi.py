from flask_restful import Resource, request
from json import loads
from myproject.models.project import Projects


class ProjectsApi(Resource):
    def post(self):
        body = request.get_json()
        try:
            Projects(**body).save()
            return {"Status": "OK"}
        except Exception as e:
            return {"Status": "Failed", "Exception": str(e)}

    def get(self):
        projects = Projects.objects()
        if projects != None:
            resp = []
            for project in projects:
                data = loads(project.to_json())
                resp.append(data)

            return {"projects": resp}, 200
        else:
            return {"projects": "Not Found"}, 404
            