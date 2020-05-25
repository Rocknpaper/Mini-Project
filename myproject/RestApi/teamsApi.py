from flask import Flask, request
from flask_restful import Resource
from json import loads
from myproject.models.teams import Teams

class TeamsApi(Resource):
    def post(self):
        body = request.get_json()
        try:
            Teams(**body).save()
            return {"Status": "OK"}, 200
        except Exception as e:
            return {"Status": "Falied", "Execption": str(e)}, 500

    def get(self):

        teams = Teams.objects()
        resp = []
        for team in teams:
            data = loads(team.to_json())
            resp.append(data)
        return resp,200
