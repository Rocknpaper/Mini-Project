from datetime import date
from random import randint



def dateToString(obj, value):
    value = str(obj[value].year) + '-' + "%.2d"%obj[value].month + "-" + str(obj[value].day)
    return value


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
    else:
        return None
    __end = "%.3d"%__random
    
    return (__prefix+__midFactor+__end)

# help = HelperFunctions()
# print(help.getPosition("UI/UX Development"))
