from django.http import HttpResponseServerError
from rest_framework import status
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import QueryDict

import requests

from frontend.forms.employee.add import AddEmployeeForm
from frontend.check_token import check_token

url_employee_list = 'http://127.0.0.1:8000/api/v1/employee/'
url_position_list = 'http://127.0.0.1:8000/api/v1/position/'
url_department_list = 'http://127.0.0.1:8000/api/v1/department/'
url_user_permissions = 'http://127.0.0.1:8000/api/v1/permissions/'
list_template = 'employee/list.html'
add_template = 'employee/add.html'
update_template = 'department/update.html'
preview_template = 'auth/preview.html'


class EmployeeListView(View):
    """Class for rendering the home page of employees"""

    @check_token(preview_template)
    def get(self, request, token):
        """Method for getting the list of employees"""

        # Getting list of employees
        api_request = requests.get(url_employee_list,
                                   headers={'Authorization': f'Token {token}'})

        if status.is_success(api_request.status_code):
            # Getting user permissions
            permissions = requests.get(url_user_permissions,
                                       headers={'Authorization': f'Token {token}'})

            return render(request, list_template, {'content': api_request.json(),
                                                   'permissions': permissions.json()})
        # If status != success -> raise ServerError
        return HttpResponseServerError()


class EmployeeCreateView(View):
    """Class for adding a new employee"""

    @check_token(preview_template)
    def get(self, request, token):
        positions = requests.get(url_position_list,
                                 headers={'Authorization': f'Token {token}'})
        departments = requests.get(url_department_list,
                                   headers={'Authorization': f'Token {token}'})
        form = AddEmployeeForm(position_list=[(position.get('url'), position.get('title'))
                                              for position in positions.json()],
                               department_list=[(department.get('url'), department.get('title'))
                                                for department in departments.json()])
        return render(request, add_template, {'form': form})

    @check_token(preview_template)
    def post(self, request, token):
        """Method for adding a new employee """

        department = requests.get(request.POST['department'],
                                  headers={'Authorization': f'Token {token}'})
        position = requests.get(request.POST['position'],
                                headers={'Authorization': f'Token {token}'})

        # Removing useless arguments
        data = QueryDict(request.body, mutable=True)
        data.pop('department')
        data.pop('position')

        form = AddEmployeeForm(data)
        # Form validation
        if form.is_valid():
            # Adding new employee
            api_request = requests.post(url_employee_list,
                                        headers={'Authorization': f'Token {token}'},
                                        files={'first_name': (None, form.data['first_name']),
                                               'second_name': (None, form.data['second_name']),
                                               'birthday': (None, form.data['birthday']),
                                               'department': (None, position.json().get('id')),
                                               'position': (None, department.json().get('id')),
                                               'salary': (None, form.data['salary']),
                                               'on_boarding_day': (None, form.data['on_boarding_day'])
                                               }
                                        )

            if status.is_success(api_request.status_code):
                return redirect('employee-list')
            return render(request, add_template, {'form': form,
                                                  'status': api_request.json()})
        else:
            return render(request, add_template, {'form': form})


# class EmployeeUpdateView(View):
#     """Class for updating departments """
#
#     @check_token(preview_template)
#     def get(self, request, token):
#         # Using AddEmployee form
#         form = AddEmployeeForm(request.GET)
#         return render(request, update_template, {'form': form,
#                                                  'url': request.GET['url']})

    # @check_token(preview_template)
    # def post(self, request, token):
    #     """Method for updating department"""
    #
    #     # Form validation
    #     form = AddDepartmentForm(request.POST)
    #     if form.is_valid():
    #         # Updating department
    #         api_request = requests.put(request.POST['url'],
    #                                    headers={'Authorization': f'Token {token}'},
    #                                    files={'title': (None, form.data['title']),
    #                                           'description': (None, form.data['description'])}
    #                                    )
    #
    #         if status.is_success(api_request.status_code):
    #             return redirect('home')
    #         # If status != success -> show errors
    #         return render(request, update_template, {'form': form,
    #                                                  'url': request.POST['url'],
    #                                                  'status': api_request.json()})
    #     else:
    #         return render(request, add_template, {'form': form})
