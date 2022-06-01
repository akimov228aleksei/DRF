from django.http import HttpResponseServerError
from rest_framework import status
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import QueryDict

import requests

from frontend.forms.vacation.add import AddVacationForm
from frontend.check_token import check_token

url_employee_list = 'http://127.0.0.1:8000/api/v1/employee/'
url_vacation_list = 'http://127.0.0.1:8000/api/v1/vacation/'
url_user_permissions = 'http://127.0.0.1:8000/api/v1/permissions/'
list_template = 'vacation/list.html'
add_template = 'vacation/add.html'
update_template = 'vacation/update.html'
preview_template = 'auth/preview.html'


class VacationListView(View):
    """Class for rendering the home page of vacation"""

    @check_token(preview_template)
    def get(self, request, token):
        """Method for getting the list of vacation"""

        # Getting list of vacation
        api_request = requests.get(url_vacation_list,
                                   headers={'Authorization': f'Token {token}'})

        if status.is_success(api_request.status_code):
            # Getting user permissions
            permissions = requests.get(url_user_permissions,
                                       headers={'Authorization': f'Token {token}'})

            return render(request, list_template, {'content': api_request.json(),
                                                   'permissions': permissions.json()})
        # If status != success -> raise ServerError
        return HttpResponseServerError()


class VacationCreateView(View):
    """Class for adding a new vacation"""

    @check_token(preview_template)
    def get(self, request, token):
        employees = requests.get(url_employee_list,
                                 headers={'Authorization': f'Token {token}'})
        form = AddVacationForm(
            employee_list=[(employee.get('id'), f"""{employee.get('first_name')} 
                                                    {employee.get('second_name')}""")
                           for employee in employees.json()])
        return render(request, add_template, {'form': form})

    @check_token(preview_template)
    def post(self, request, token):
        """ Method for adding a new vacation """
        # Removing useless arguments
        data = QueryDict(request.body, mutable=True)
        data.pop('employee')

        form = AddVacationForm(data)
        # Form validation
        if form.is_valid():
            # Adding new vacation
            api_request = requests.post(url_vacation_list,
                                        headers={'Authorization': f'Token {token}'},
                                        files={'employee': (None, request.POST['employee']),
                                               'start_date': (None, form.data['start_date']),
                                               'end_date': (None, form.data['end_date'])
                                               }
                                        )

            if status.is_success(api_request.status_code):
                return redirect('vacation-list')
            return render(request, add_template, {'form': form,
                                                  'status': api_request.json()})
        else:
            return render(request, add_template, {'form': form,
                                                  'errors': form.errors})


class VacationUpdateView(View):
    """ Class for updating vacation"""

    @check_token(preview_template)
    def get(self, request, token):
        employees = requests.get(url_employee_list,
                                 headers={'Authorization': f'Token {token}'})

        form = AddVacationForm(employee_list=[(employee.get('id'), f"""{employee.get('first_name')} 
                                                    {employee.get('second_name')}""")
                               for employee in employees.json()],
                               data=request.GET)
        # Using AddVacationForm
        return render(request, update_template, {'form': form,
                                                 'url': request.GET['url']})

    @check_token(preview_template)
    def post(self, request, token):
        """Method for updating vacation"""

        # Removing useless arguments
        data = QueryDict(request.body, mutable=True)
        data.pop('employee')

        # Form validation
        form = AddVacationForm(data)
        if form.is_valid():
            # Updating vacation
            api_request = requests.put(request.POST['url'],
                                       headers={'Authorization': f'Token {token}'},
                                       files={'first_name': (None, form.data['first_name']),
                                              'second_name': (None, form.data['second_name']),
                                              'birthday': (None, form.data['birthday']),
                                              'department': (None, request.POST['department']),
                                              'position': (None, request.POST['position']),
                                              'salary': (None, form.data['salary']),
                                              'on_boarding_day': (None, form.data['on_boarding_day'])
                                              })
            if status.is_success(api_request.status_code):
                return redirect('employee-list')
            # If status != success -> show errors
            return render(request, update_template, {'form': form,
                                                     'url': request.POST['url'],
                                                     'status': api_request.json()})
        else:
            return render(request, add_template, {'form': form,
                                                  'errors': form.errors})


class VacationDeleteView(View):
    """ Class for deleting vacation """

    @check_token(preview_template)
    def post(self, request, token):
        """Method for deleting vacation"""

        # Deleting vacation
        api_request = requests.delete(request.POST['url'],
                                      headers={'Authorization': f'Token {token}'})
        if status.is_success(api_request.status_code):
            return redirect('vacation-list')
        # If status != success -> raise ServerError
        return HttpResponseServerError()
