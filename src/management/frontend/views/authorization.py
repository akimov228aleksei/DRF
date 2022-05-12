from rest_framework import status
from django.shortcuts import render, redirect
from django.views.generic import View
import requests
from ..forms.authorization import AuthorizationForm


class AuthorizationView(View):
    """Class for authorization"""

    template_name = 'authorization.html'

    def get(self, request):
        form = AuthorizationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AuthorizationForm(request.POST)
        if form.is_valid():
            r = requests.post('http://127.0.0.1:8000/api/v1/auth/token/login/',
                              files={'username': (None, form.data['username']),
                                     'password': (None, form.data['password'])})

            if status.is_success(r.status_code) or status.is_redirect(r.status_code):
                response = redirect('home')
                response.set_cookie('Token', r.json().get('auth_token'))
                return response
            return render(request, self.template_name, {'form': form, 'status': r.text})
        else:
            return render(request, self.template_name, {'form': form})
