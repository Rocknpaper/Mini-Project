from flask_restful import Resource, request
from json import loads
from myproject.models.employeeLogin import EmployeeLogin
from myproject.models.employeeAttendance import EmployeeAttendance, AttendanceBluePrint, WeeklyUpdate, DaysOfTheWeek

class EmployeeAttendanceApi(Resource):
    def post(self, empID):
        body = request.get_json()
        try:
            employee = EmployeeLogin.objects(_id=empID).first()
            if employee != None:
                day = DaysOfTheWeek(remark = body["remark"])
                week = WeeklyUpdate(weeklyAttendance=[day])
                blpt = AttendanceBluePrint(week=[week])
                EmployeeAttendance(_id=empID, employeeAttendance=[blpt]).save()
                return {"Status": "OK"}, 200
            else:
                return {"emplpoyee": "Not Found"}, 404
        except Exception as e:
            return {"Status": "Failed", "Exception": str(e)}, 500

    def get(self, empID):
        employee = EmployeeLogin.objects(_id=empID).first()
        if employee != None:
            attendance = EmployeeAttendance.objects(_id=empID)
            return loads(attendance.to_json()), 200
        else:
            return {"employee": "Not Found"}, 400
                