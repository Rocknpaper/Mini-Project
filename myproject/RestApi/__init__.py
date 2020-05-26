from myproject import app
from flask_restful import Api
from myproject.RestApi.employeeLoginApi import EmployeeLoginApi
from myproject.RestApi.employeePersonalApi import EmployeePersonalApi
from myproject.RestApi.teamsApi import TeamsApi
from myproject.RestApi.projectsApi import ProjectsApi
from myproject.RestApi.departmentsApi import DepartmentsApi
from myproject.RestApi.employeeWorkDetailsApi import EmployeeWorkDetailsApi
from myproject.RestApi.employeeTeamDetailsApi import EmployeeTeamDetailsApi
from myproject.RestApi.employeeSalaryApi import EmployeeSalaryApi
from myproject.RestApi.employeeAttendanceApi import EmployeeAttendanceApi
from myproject.RestApi.employeeLeaveApi import EmployeeLeavesApi

api = Api(app)

api.add_resource(EmployeeLoginApi, "/emp")
api.add_resource(EmployeePersonalApi, "/emppersonal/<empID>")
api.add_resource(TeamsApi, "/team")
api.add_resource(ProjectsApi, "/project")
api.add_resource(DepartmentsApi, "/department")
api.add_resource(EmployeeWorkDetailsApi, "/work/<empID>")
api.add_resource(EmployeeTeamDetailsApi, "/teamdet/<empID>")
api.add_resource(EmployeeSalaryApi, "/salary/<empID>")
api.add_resource(EmployeeAttendanceApi, "/attendance/<empID>")
api.add_resource(EmployeeLeavesApi, "/leave/<empID>")