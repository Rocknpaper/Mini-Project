from flask_restful import Resource, request
from json import loads
from myproject.models.employeeLogin import EmployeeLogin
from myproject.models.employeeSalary import EmployeeSalary, ApprasialsandAllowance


class EmployeeSalaryApi(Resource):
    
    def post(self, empID):
        body = request.get_json()

        employee = EmployeeLogin.objects(_id=empID).first()
        if employee != None:
            try:
                apprasials = ApprasialsandAllowance(year=body["appraisalYear"], amount=body["appraisalAmount"])
                allowances = ApprasialsandAllowance(year=body["allowanceYear"], amount=body["allowanceAmount"])
                remList = ["appraisalYear", "appraisalAmount", "allowanceYear", "allowanceAmount"]

                [body.pop(key) for key in remList]
                
                body["_id"] = empID
                body["apprasialsOverTheYears"] = [apprasials]
                body["allowancesOverTheYears"] = [allowances]
                
                EmployeeSalary(**body).save()
                return {"Status": "OK"}, 200
            
            except Exception as e:
                return {"Status": "Falied", "Exception": str(e)}, 400
        else:
            return {"employee": "Not Found"}, 404

    def get(self, empID):
        employee = EmployeeLogin.objects(_id=empID).first()
        if employee != None:
            salary = EmployeeSalary.objects(_id=empID).first()
            salary["employeePF"] = salary.employeeSalary * (salary.employeePF/100)
            data = loads(salary.to_json())
            return data, 200

        else:
            return{"employee": "Not Found"}, 404
