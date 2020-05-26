from myproject import db
from myproject.helper.helpers import getYears, getMonths, getWeeks, getDate, getDay, giveRemarks


class DaysOfTheWeek(db.EmbeddedDocument):
    date = db.StringField(required=True, default=getDate())
    day = db.StringField(required=True, default=getDay())
    remark = db.StringField(required=True, default=giveRemarks())
    # sun = db.StringField(required=True, default=AttendanceRemarks.HOLIDAY)
    # mon = db.StringField(required=True, default=AttendanceRemarks.NOT_ENTERED)
    # tue = db.StringField(required=True, default=AttendanceRemarks.NOT_ENTERED)
    # wed = db.StringField(required=True, default=AttendanceRemarks.NOT_ENTERED)
    # thur = db.StringField(required=True, default=AttendanceRemarks.NOT_ENTERED)
    # fri = db.StringField(required=True, default=AttendanceRemarks.NOT_ENTERED)
    # sat = db.StringField(required=True, default=AttendanceRemarks.NOT_ENTERED)
    
class WeeklyUpdate(db.EmbeddedDocument):
    weekNo = db.StringField(required=True, default=getWeeks())
    weeklyAttendance = db.ListField(db.EmbeddedDocumentField(DaysOfTheWeek), required=True)
    meta = {
        "indexes": ["weekNo"]
    }

class AttendanceBluePrint(db.EmbeddedDocument):
    year = db.StringField(required=True, default=getYears())
    month = db.StringField(required=True, default=getMonths())
    week = db.ListField(db.EmbeddedDocumentField(WeeklyUpdate) ,required=True)
  
class EmployeeAttendance(db.Document):
    _id = db.StringField(required=True)
    employeeAttendance = db.ListField(db.EmbeddedDocumentField(AttendanceBluePrint))
    meta = {
        "indexes": ["employeeAttendance.year", "employeeAttendance.month", "employeeAttendance.week.weekNo"]
    }
    