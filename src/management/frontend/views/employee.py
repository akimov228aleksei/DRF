from django.http import HttpResponseServerError
from rest_framework import status
from django.shortcuts import render, redirect
from django.views.generic import View
import requests

url_employee_list = 'http://127.0.0.1:8000/api/v1/employee/'
url_user_permissions = 'http://127.0.0.1:8000/api/v1/permissions/'
url_department_list = 'http://127.0.0.1:8000/api/v1/department/'
url_position_list = 'http://127.0.0.1:8000/api/v1/position/'
list_template = 'employee/list.html'
add_template = 'department/add.html'
update_template = 'department/update.html'
preview_template = 'auth/preview.html'


class EmployeeListView(View):
    """Class for rendering the home page of employees"""

    def get(self, request):
        """Method for getting the list of employees"""

        # Getting token from cookies
        token = request.COOKIES.get("Token")
        # If token is absent -> redirect to authorization
        if not token:
            return render(request, preview_template)
        # Getting list of employees
        api_request = requests.get(url_employee_list,
                                   headers={'Authorization': f'Token {token}'})

        if status.is_success(api_request.status_code):
            # Getting list of departments
            departments = requests.get(url_department_list,
                                       headers={'Authorization': f'Token {token}'})

            # Getting list of positions
            positions = requests.get(url_position_list,
                                     headers={'Authorization': f'Token {token}'})

            # Insert department.title instead of url
            response = api_request.json()
            for employee in response:
                for department in departments.json():
                    if employee['department'] == department['url']:
                        employee['department'] = department['title']

            # Insert position.title instead of url
            for employee in response:
                for position in positions.json():
                    if employee['position'] == position['url']:
                        employee['position'] = position['title']

            # Getting user permissions
            permissions = requests.get(url_user_permissions,
                                       headers={'Authorization': f'Token {token}'})

            return render(request, list_template, {'content': response,
                                                   'permissions': permissions.json()})
        # If status != success -> rise ServerError
        return HttpResponseServerError()
