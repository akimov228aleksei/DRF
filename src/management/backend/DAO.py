"""The file contains all the available methods
for accessing the database"""
from backend.models import employee


class EmployeeDAO:
    """The class contains methods for accessing the employee table"""

    @staticmethod
    def get_list():
        """The method returns all data from the employee table"""
        return employee.Employee.objects.all()

    @staticmethod
    def filter_department(value):
        """The method returns all employees belonging to a specific department"""
        return employee.Employee.objects.filter(department=value)
