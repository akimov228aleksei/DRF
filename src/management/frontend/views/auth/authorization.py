from rest_framework import status
from django.shortcuts import render, redirect
from django.views.generic import View
import requests
from frontend.forms.auth.authorization import AuthorizationForm


class AuthorizationView(View):
    """Class for authorization"""

    template_name = 'auth/authorization.html'

    def get(self, request):
        # If user is authorized, then redirect on 'home'
        if request.COOKIES.get('Token'):
            return redirect('home')
        form = AuthorizationForm
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AuthorizationForm(request.POST)
        if form.is_valid():
            api_request = requests.post('http://127.0.0.1:8000/api/v1/auth/token/login/',
                                        files={'username': (None, form.data['username']),
                                               'password': (None, form.data['password'])})

            if status.is_success(api_request.status_code):
                # If token is received, then it is added to the cookies
                response = redirect('home')
                response.set_cookie('Token', api_request.json().get('auth_token'))
                return response
            return render(request, self.template_name, {'form': form,
                                                        'status': api_request.json()})
        else:
            return render(request, self.template_name, {'form': form})
