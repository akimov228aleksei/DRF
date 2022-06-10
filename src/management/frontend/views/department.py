from django.http import HttpResponseServerError
from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.generic import View
from rest_framework import status
import requests

from frontend.forms.department.add import AddDepartmentForm
from frontend.check_token import check_token

url_department_list = 'http://127.0.0.1:8000/api/v1/department/'
url_user_permissions = 'http://127.0.0.1:8000/api/v1/permissions/'
list_template = 'department/list.html'
add_template = 'department/add.html'
update_template = 'department/update.html'
detail_template = 'department/detail.html'
preview_template = 'auth/preview.html'


class DepartmentListView(View):
    """Class for rendering the home page of departments"""

    @check_token(html_to_render=preview_template)
    def get(self, request, token):
        """Method for getting the list of departments"""

        api_request = requests.get(url_department_list,
                                   headers={'Authorization': f'Token {token}'})
        if status.is_success(api_request.status_code):
            # Getting user permissions
            permissions = requests.get(url_user_permissions,
                                       headers={'Authorization': f'Token {token}'})

            return render(request, list_template, {'content': api_request.json(),
                                                   'permissions': permissions.json()})
        # If status != success -> raise ServerError
        return HttpResponseServerError()


class DepartmentDetailView(View):
    """Class for showing detail list of departments"""

    @check_token(preview_template)
    def get(self, request, token):
        api_request = requests.get(request.GET['url'],
                                   headers={'Authorization': f'Token {token}'})
        if status.is_success(api_request.status_code):
            return render(request, detail_template, {'content': api_request.json()})
        # If status != success -> raise ServerError
        return HttpResponseServerError()


class DepartmentCreateView(View):
    """Class for adding a new department"""

    @check_token(preview_template)
    def get(self, request, token):
        form = AddDepartmentForm
        return render(request, add_template, {'form': form})

    @check_token(preview_template)
    def post(self, request, token):
        """Method for adding a new department"""

        # Form validation
        form = AddDepartmentForm(request.POST)
        if form.is_valid():
            # Adding new department
            api_request = requests.post(url_department_list,
                                        headers={'Authorization': f'Token {token}'},
                                        files={'title': (None, form.data['title']),
                                               'description': (None, form.data['description'])}
                                        )

            if status.is_success(api_request.status_code):
                return redirect('home')
            return render(request, add_template, {'form': form,
                                                  'status': api_request.json()})
        else:
            return render(request, add_template, {'form': form,
                                                  'errors': form.errors})


class DepartmentUpdateView(View):
    """Class for updating departments """

    @check_token(preview_template)
    def get(self, request, token):
        # Using AddDepartment form
        form = AddDepartmentForm(request.GET)
        return render(request, update_template, {'form': form,
                                                 'url': request.GET['url']})

    @check_token(preview_template)
    def post(self, request, token):
        """Method for updating department"""

        # Form validation
        form = AddDepartmentForm(request.POST)
        if form.is_valid():
            # Updating department
            api_request = requests.put(request.POST['url'],
                                       headers={'Authorization': f'Token {token}'},
                                       files={'title': (None, form.data['title']),
                                              'description': (None, form.data['description'])}
                                       )

            if status.is_success(api_request.status_code):
                return redirect('home')
            # If status != success -> show errors
            return render(request, update_template, {'form': form,
                                                     'url': request.POST['url'],
                                                     'status': api_request.json()})
        else:
            return render(request, add_template, {'form': form,
                                                  'errors': form.errors})


class DepartmentDeleteView(View):
    """Class for deleting departments """

    @check_token(preview_template)
    def post(self, request, token):
        """Method for deleting department"""
        api_request = requests.delete(request.POST['url'],
                                      headers={'Authorization': f'Token {token}'})
        if status.is_success(api_request.status_code):
            return redirect('home')
        # Display warning window
        elif api_request.status_code == status.HTTP_405_METHOD_NOT_ALLOWED:
            return redirect('http://127.0.0.1:8000/#window')
        # If status != success -> raise ServerError
        return HttpResponseServerError()
