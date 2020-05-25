from flask_restful import Resource, request
from myproject.models.employeeLogin import EmployeeLogin
from myproject.models.employeeTeamDetails import EmployeeTeamDetails
from myproject.models.employeePastTeams import EmployeePastTeams


class EmployeeTeamDetailsApi(Resource):
    def post(self, empID):
        body = request.get_json()
        employee = EmployeeLogin.objects(_id=empID).first()
        if employee != None:
            try:
                emp = EmployeePastTeams(_id=body["teamId"], joinedTeam=body["joinedTeam"], leftTeam=body["leftTeam"])
                del body["teamId"], body["joinedTeam"], body["leftTeam"]
                body["_id"] = empID
                body["teamsWorked"] = [emp]
                # TODO: Change it to meaningful
                # body["prjectsWorked"] = "PRO240520935"
                EmployeeTeamDetails(**body).save()
                return {"Status": "OK"}, 200

            except Exception as e:
                return {"Status": "Failed", "Exception": str(e)}, 500

        else:
            {"Employee": "Not Found"}, 404
        

