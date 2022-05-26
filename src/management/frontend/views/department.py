from django.http import HttpResponseServerError
from rest_framework import status
from django.shortcuts import render, redirect
from django.views.generic import View
import requests

from frontend.forms.department.add import AddDepartmentForm

url_department_list = 'http://127.0.0.1:8000/api/v1/department/'
url_user_permissions = 'http://127.0.0.1:8000/api/v1/permissions/'
list_template = 'department/list.html'
add_template = 'department/add.html'
update_template = 'department/update.html'
preview_template = 'auth/preview.html'


class DepartmentListView(View):
    """Class for rendering the home page of departments"""

    def get(self, request):
        """Method for getting the list of departments"""

        # Getting token from cookies
        token = request.COOKIES.get("Token")
        # If token is absent -> redirect to authorization
        if not token:
            return render(request, preview_template)
        # Getting list of departments
        api_request = requests.get(url_department_list,
                                   headers={'Authorization': f'Token {token}'})

        if status.is_success(api_request.status_code):
            # Getting user permissions
            permissions = requests.get(url_user_permissions,
                                       headers={'Authorization': f'Token {token}'})

            return render(request, list_template, {'content': api_request.json(),
                                                   'permissions': permissions.json()})
        # If status != success -> rise ServerError
        return HttpResponseServerError()

# class DepartmentDetailView(View):
#     """Class for showing detail list of departments"""
#
#     def post(self, request):
#         # Getting token from cookies
#         token = request.COOKIES.get("Token")
#         # If token is absent -> redirect to authorization
#         if not token:
#             return render(request, preview_template)
#         # Getting detail list of departments
#         api_request = requests.get(url,
#                                    headers={'Authorization': f'Token {token}'})


class DepartmentCreateView(View):
    """Class for adding a new department"""

    def get(self, request):
        # If token is absent -> redirect to authorization
        if not request.COOKIES.get('Token'):
            return render(request, preview_template)
        form = AddDepartmentForm
        return render(request, add_template, {'form': form})

    def post(self, request):
        """Method for adding a new department"""

        # Getting token from cookies
        token = request.COOKIES.get("Token")
        # If token is absent -> redirect to authorization
        if not token:
            return render(request, preview_template)
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
            return render(request, add_template, {'form': form})


class DepartmentUpdateView(View):
    """Class for updating departments """

    def get(self, request):
        # If token is absent -> redirect to authorization
        if not request.COOKIES.get('Token'):
            return render(request, preview_template)
        # Using AddDepartment form
        form = AddDepartmentForm(request.GET)
        return render(request, update_template, {'form': form,
                                                 'url': request.GET['url']})

    def post(self, request):
        """Method for updating department"""

        # Getting token from cookies
        token = request.COOKIES.get("Token")
        # If token is absent -> redirect to authorization
        if not token:
            return render(request, preview_template)
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
            return render(request, add_template, {'form': form})


class DepartmentDeleteView(View):
    """Class for deleting departments """

    def post(self, request):
        """Method for deleting department"""

        # Getting token from cookies
        token = request.COOKIES.get("Token")
        # If token is absent -> redirect to authorization
        if not token:
            return render(request, preview_template)
        # Deleting department
        api_request = requests.delete(request.POST['url'],
                                      headers={'Authorization': f'Token {token}'})
        if status.is_success(api_request.status_code):
            return redirect('home')
        # If status != success -> rise ServerError
        return HttpResponseServerError()