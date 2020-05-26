from flask_restful import Resource, request
from json import loads
from myproject.models.employeeLogin import EmployeeLogin
from myproject.models.employeeLeaves import EmployeeLeaves, LeaveTemplate
from myproject.helper.helpers import dateDiffernce, dateToString, leavesHelper

class EmployeeLeavesApi(Resource):
    def post(self, empID):
        body = request.get_json()
        try:
            employee = EmployeeLogin.objects(_id=empID).first()
            if employee != None:
                leave = LeaveTemplate(**body)
                EmployeeLeaves(_id=empID, leaves=[leave]).save()
                return {"Status": "OK"}, 200
            else:
                return {"employee": "Not Found"}, 404
        except Exception as e:
            return {"Status": "Failed", "Execption": str(e)}, 500

    def get(self, empID):
        employee = EmployeeLogin.objects(_id=empID).first()
        if employee != None:
            leave = EmployeeLeaves.objects().first()
            resp = []
            fromDate = []
            toDate =[]
            for date in leave.leaves:
                fromDate.append(date.leaveFrom)
                toDate.append(date.leaveTo)

            data = loads(leave.to_json())
            for i, d in enumerate(data["leaves"]):
                d["leaveFrom"] = leavesHelper(str(fromDate[i]))
                d["leaveTo"] = leavesHelper(str(toDate[i]))
                d["numberOfDays"] = dateDiffernce(fromDate[i], toDate[i])
            return data, 200

        else:
            return{"employee": "Not Found"}, 404