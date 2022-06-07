from django.http import HttpResponseServerError
from rest_framework import status
from django.shortcuts import render, redirect
from django.views.generic import View

import requests

from frontend.forms.position.add import AddPositionForm
from frontend.check_token import check_token

url_employee_list = 'http://127.0.0.1:8000/api/v1/employee/'
url_position_list = 'http://127.0.0.1:8000/api/v1/position/'
url_department_list = 'http://127.0.0.1:8000/api/v1/department/'
url_user_permissions = 'http://127.0.0.1:8000/api/v1/permissions/'
list_template = 'position/list.html'
add_template = 'position/add.html'
update_template = 'position/update.html'
preview_template = 'auth/preview.html'


class PositionListView(View):
    """Class for rendering the home page of positions"""

    @check_token(preview_template)
    def get(self, request, token):
        """Method for getting the list of positions"""

        # Getting user permissions
        permissions = requests.get(url_user_permissions,
                                   headers={'Authorization': f'Token {token}'})

        # If user has permissions -> show all records
        is_active = 'backend.change_position' not in permissions.json()

        # Getting list of positions
        api_request = requests.get(url_position_list,
                                   headers={'Authorization': f'Token {token}'},
                                   params={'active': is_active})

        if status.is_success(api_request.status_code):
            return render(request, list_template, {'content': api_request.json(),
                                                   'permissions': permissions.json()})
        # If status != success -> raise ServerError
        return HttpResponseServerError()


class PositionCreateView(View):
    """Class for adding a new position"""

    @check_token(preview_template)
    def get(self, request, token):
        form = AddPositionForm
        return render(request, add_template, {'form': form})

    @check_token(preview_template)
    def post(self, request, token):
        """Method for adding a new position"""

        # Form validation
        form = AddPositionForm(request.POST)
        if form.is_valid():
            # Adding new position
            api_request = requests.post(url_position_list,
                                        headers={'Authorization': f'Token {token}'},
                                        files={'title': (None, form.data['title']),
                                               'max_salary': (None, form.data['max_salary']),
                                               'active': (None, form.data.get('active', False))}
                                        )

            if status.is_success(api_request.status_code):
                return redirect('position-list')
            return render(request, add_template, {'form': form,
                                                  'status': api_request.json()})
        else:
            return render(request, add_template, {'form': form,
                                                  'errors': form.errors})


class PositionUpdateView(View):
    """Class for updating positions """

    @check_token(preview_template)
    def get(self, request, token):
        # Using AddPosition form
        form = AddPositionForm(request.GET)
        return render(request, update_template, {'form': form,
                                                 'url': request.GET['url']})

    @check_token(preview_template)
    def post(self, request, token):
        """ Method for updating positions """

        # Form validation
        form = AddPositionForm(request.POST)
        if form.is_valid():
            # Updating position
            api_request = requests.put(request.POST['url'],
                                       headers={'Authorization': f'Token {token}'},
                                       files={'title': (None, form.data['title']),
                                              'max_salary': (None, form.data['max_salary']),
                                              'active': (None, form.data.get('active', False))}
                                       )

            if status.is_success(api_request.status_code):
                return redirect('position-list')
            # If status != success -> show errors
            return render(request, update_template, {'form': form,
                                                     'url': request.POST['url'],
                                                     'status': api_request.json()})
        else:
            return render(request, add_template, {'form': form,
                                                  'errors': form.errors})


class PositionDeleteView(View):
    """Class for deleting positions """

    @check_token(preview_template)
    def post(self, request, token):
        """Method for deleting positions"""

        # Deleting position
        api_request = requests.delete(request.POST['url'],
                                      headers={'Authorization': f'Token {token}'})
        if status.is_success(api_request.status_code):
            return redirect('position-list')
        # If status != success -> raise ServerError
        return HttpResponseServerError()
