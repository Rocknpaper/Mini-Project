from datetime import date, datetime
from random import randint
from calendar import day_name
from enum import Enum


def dateToString(obj, value):
    value = str(obj[value].year) + '-' + "%.2d"%obj[value].month + "-" + str(obj[value].day)
    return value

def leavesHelper(date):
    return date[0:10]


def getPosition(dept):
    if dept == "UI/UX Development":
        position = "Designer"
    elif dept == "Research And Development":
        position = "Engineer"
    elif dept == "Software Development":
        position == "Developer"
    return position



def generateUniqueId(target):
    __today = date.today()
    if target == "E":
        __prefix = "EMP"
        __midFactor = "%.2d"%__today.month + str(__today.day)
        __random = randint(200, 999)
    elif target == "T":
        __prefix = "TM"
        __midFactor = str(__today.year)[-2:] + str(__today.day)
        __random = randint(1, 999)
    elif target == "P":
        __prefix = "PRO" 
        __midFactor = str(__today.day) + "%.2d"%__today.month + str(__today.year)[-2:] 
        __random = randint(1, 999)
    elif target == "L":
        __prefix = "LEV"
        __midFactor = str(__today.day) + "%.2d"%__today.month + str(__today.year)[-2:]
        __random = randint(1, 99999)
    elif target == "H":
        __prefix = "HOL"
        __midFactor = str(__today.day) + "%.2d"%__today.month + str(__today.year)[-2:]
        __random = randint(1, 99999)
    elif target == "M":
        __prefix = "MED"
        __midFactor = str(__today.day) + "%.2d"%__today.month + str(__today.year)[-2:]
        __random = randint(1, 99999)
    elif target == "V":
        __prefix = "VAC"
        __midFactor = str(__today.day) + "%.2d"%__today.month + str(__today.year)[-2:]
        __random = randint(1, 99999)
    else:
        return None
    __end = "%.3d"%__random
    
    return (__prefix+__midFactor+__end)

def getYears():
    __year = datetime.now()
    return str(__year.year)

def getMonths():
    __month = datetime.now()
    return str(__month.strftime("%B"))

def getWeeks():
    __day = datetime.now()
    return str(__day.isocalendar()[1] - __day.replace(day=1).isocalendar()[1] + 1)

def getDate():
    __date = datetime.now()
    return str(__date.today())[8:10]

def getDay():
    my_date = date.today()
    return str(day_name[my_date.weekday()])

class AttendanceRemarks(Enum):
    PRESENT = "P"
    ABESENT = "A"
    HOLIDAY = "H"
    NOT_ENTERED = "N"
    GOVT_HOLIDAY = "GH"
    MEDICAL_LEAVE = "ML"
    PERSONAL_LEAVE = "PSL"
    PAID_LEAVE = "PL"
    ON_VACATION = "OV"

def giveRemarks(day = getDay()):
    if day == "Sunday":
        return AttendanceRemarks.HOLIDAY.value
    else:
        return AttendanceRemarks.NOT_ENTERED.value

def dateDiffernce(fromDate, toDate):
    __days = toDate - fromDate
    return __days.days

# help = HelperFunctions()
# print(help.getPosition("UI/UX Development"))
# date1 = date.today()
# date2 = date(2020, 5, 16)

# print(len(generateUniqueId("L")))
